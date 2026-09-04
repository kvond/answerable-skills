#!/usr/bin/env python3
"""Mark live Google Slides decks in place through the Slides API.

Companion to embed_markers.py. embed_markers.py plans and stamps .pptx files;
this file takes that plan (build_plan) and applies it to the Google Slides
deck itself, so the file ID, and every /copy link that points at it, stays
the same and nothing passes through a .pptx conversion.

Runs inside the Composio remote workbench, where proxy_execute() carries the
Drive connection's token; the Slides API accepts the Drive scope. First run
2026-09-04 on all 26 Biology class decks (Cycles 01a-20), verified by
re-exporting each deck and counting markers against its inventory line.

Steps per deck: (1) delete every existing marker run and every inventory
shape (whole shape, so no stale "NOTES=..." text survives); (2) re-read the
deck; (3) append each marker as 1pt white Arial after its label text, matched
by the label's text on the planned slide; (4) create the inventory text box
on slide 1.
"""
import re, json, os
from pptx import Presentation
import embed_markers as em
MARK_RE=re.compile(r"\[\[[A-Z-]+:[^\]]*\]\]")
PPTX='application/vnd.openxmlformats-officedocument.presentationml.presentation'
FIELDS="slides(objectId,pageElements(objectId,shape(text(textElements(startIndex,endIndex,textRun(content))))))"

def build_plan(fn):
    m=re.search(r"Cycle\s*0?(\d+)\s*([A-Za-z])?", os.path.basename(fn)); cyc="C%02d%s"%(int(m.group(1)),(m.group(2) or "").upper())
    prs=Presentation(fn); em.strip_markers(prs)   # plan on a clean copy in memory
    marks,bank,_=em.plan(prs,cyc)
    items=[{"slide":i,"label":em.texts(lab).strip(),"kind":k,"qid":q} for i,lab,k,q in marks]
    bk=[{"slide":i,"label":em.texts(sh).strip(),"term":t} for i,sh,t in bank]
    inv=em.inventory_line(cyc,marks,bank)
    return {"cyc":cyc,"marks":items,"bank":bk,"inventory":inv}

def u16(s): return len(s.encode("utf-16-le"))//2

def norm(s): return re.sub(r"\s+"," ",MARK_RE.sub("",s or "")).strip()

def get_pres(pid):
    res,err=proxy_execute("GET",f"https://slides.googleapis.com/v1/presentations/{pid}","googledrive",query_params={"fields":FIELDS})
    if err: raise RuntimeError(err)
    return res

def elem_text(el):
    tes=el.get("shape",{}).get("text",{}).get("textElements",[])
    runs=[(te.get("startIndex",0),te["textRun"]["content"]) for te in tes if "textRun" in te]
    full="".join(c for _,c in runs); end=max([te.get("endIndex",0) for te in tes],default=0)
    return full,runs,end

def batch(pid,reqs):
    if not reqs: return {}
    res,err=proxy_execute("POST",f"https://slides.googleapis.com/v1/presentations/{pid}:batchUpdate","googledrive",body={"requests":reqs},headers={"Content-Type":"application/json"})
    if err: raise RuntimeError(str(err)[:300]+" :: "+str(res)[:300])
    return res

def style_req(oid,start,end):
    return {"updateTextStyle":{"objectId":oid,"textRange":{"type":"FIXED_RANGE","startIndex":start,"endIndex":end},"style":{"fontSize":{"magnitude":1,"unit":"PT"},"fontFamily":"Arial","foregroundColor":{"opaqueColor":{"rgbColor":{"red":1,"green":1,"blue":1}}}},"fields":"fontSize,fontFamily,foregroundColor"}}

def mark_slides(pid, plan, dry=False):
    log=[]
    pres=get_pres(pid); slides=pres["slides"]
    # pass 1: strip
    reqs=[]
    for s in slides:
        for el in s.get("pageElements",[]):
            full,runs,end=elem_text(el)
            if not full: continue
            if "MARKER-INVENTORY" in full or ("NOTES=" in full and "DRAFT=" in full and "_IDS=" in full):
                reqs.append({"deleteObject":{"objectId":el["objectId"]}}); log.append(f"delete inventory shape on slide {slides.index(s)+1}"); continue
            dels=[]
            for st,content in runs:
                for m in MARK_RE.finditer(content):
                    a=st+u16(content[:m.start()]); b=a+u16(m.group(0))
                    # also eat leading spaces before the marker
                    lead=len(content[:m.start()])-len(content[:m.start()].rstrip(" ")); a-=lead
                    dels.append((a,b))
            for a,b in sorted(dels,reverse=True):
                reqs.append({"deleteText":{"objectId":el["objectId"],"textRange":{"type":"FIXED_RANGE","startIndex":a,"endIndex":b}}})
    nstrip=len(reqs)
    if reqs and not dry: batch(pid,reqs)
    # pass 2: insert
    pres=get_pres(pid); slides=pres["slides"]; reqs=[]; missing=[]
    def find(sidx,label):
        cands=[]
        for el in slides[sidx].get("pageElements",[]):
            full,runs,end=elem_text(el)
            if not full: continue
            if norm(full)==norm(label): cands.append((el["objectId"],end))
        if not cands:
            for el in slides[sidx].get("pageElements",[]):
                full,runs,end=elem_text(el)
                if full and norm(label) and (norm(full).startswith(norm(label)[:40]) or norm(label).startswith(norm(full)[:40]) and len(norm(full))>10): cands.append((el["objectId"],end))
        return cands[0] if len(cands)==1 else (cands[0] if cands else None)
    for it in plan["marks"]+[{"slide":b["slide"],"label":b["label"],"marker":f"[[BANK:{plan['cyc']}:{b['term']}]]"} for b in plan["bank"]]:
        marker=it.get("marker") or f"[[{it['kind']}:{plan['cyc']}:{it['qid']}]]"
        hit=find(it["slide"],it["label"])
        if not hit: missing.append((it["slide"]+1,it["label"][:40],marker)); continue
        oid,end=hit; ins="  "+marker; at=end-1
        reqs.append({"insertText":{"objectId":oid,"insertionIndex":at,"text":ins}}); reqs.append(style_req(oid,at,at+u16(ins)))
    s1=slides[0]["objectId"]; inv_id="marker_inventory_"+re.sub(r"[^A-Za-z0-9]","",plan["cyc"])
    reqs.append({"createShape":{"objectId":inv_id,"shapeType":"TEXT_BOX","elementProperties":{"pageObjectId":s1,"size":{"width":{"magnitude":72,"unit":"PT"},"height":{"magnitude":9,"unit":"PT"}},"transform":{"scaleX":1,"scaleY":1,"translateX":0,"translateY":0,"unit":"PT"}}}})
    reqs.append({"insertText":{"objectId":inv_id,"insertionIndex":0,"text":plan["inventory"]}}); reqs.append(style_req(inv_id,0,u16(plan["inventory"])))
    if not dry: batch(pid,reqs)
    return {"stripped":nstrip,"inserted":len(plan["marks"])+len(plan["bank"])-len(missing),"missing":missing,"log":log}
