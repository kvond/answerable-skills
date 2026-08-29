#!/usr/bin/env python3
"""Editing Contract Generator (Katherine Von Duyke)

Creates two files you can upload alongside a chapter:
  1) editorial_contract.md   (human-readable)
  2) editorial_contract.json (machine-readable)

Usage:
  python editing_contract_generator.py --outdir .
  python editing_contract_generator.py --outdir ./contracts --version 2026-01-16
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any, Dict, List


def contract(version: str) -> Dict[str, Any]:
    """Return the current editorial contract as a structured dict."""

    return {
        "contract_name": "KVD Editorial Contract",
        "version": version,
        "generated_on": date.today().isoformat(),
        "scope": "Always active editorial law for the manuscript unless explicitly superseded.",
        "core_commitments": {
            "authorial_control": [
                "No free rewrites.",
                "Wording changes only by explicit request or clear service to the author’s established voice and intent.",
                "If a change risks violating this contract, it is flagged, not executed.",
            ],
            "voice": [
                "Warm, invitational, intellectually serious.",
                "No ChatGPT smoothing.",
                "Moral clarity without argument-winning.",
            ],
            "nuance_and_story": [
                "Preserve anecdotes, classroom vignettes, and homeschooling stories with ethical depth (misrecognition, displacement of the knower, institutional pressure).",
            ],
            "conceptual_precision": [
                "Agency ≠ motivation ≠ autonomy ≠ authorship.",
                "Epistemic agency ≠ partially correct answers.",
                "Sense-making ≠ meaning-making (clarify briefly when relevant).",
                "Dialogism is a hinge with a tool-and-boundary ethic (powerful, not universal).",
            ],
            "audience": [
                "Teachers, parents, innovators — without sanding down intellectual seriousness.",
            ],
        },
        "editing_mechanics": {
            "no_silent_fill_in": {
                "rule": "If something feels missing, insert bracketed placeholders only. No new prose that pretends to be the author.",
                "allowed_placeholders": [
                    "[BRIDGE NEEDED: explain how X leads to Y—what’s the hinge?]",
                    "[STORY SLOT: a 6–10 line vignette that shows students guessing to survive / trained to guess.]",
                    "[CONCEPTUAL NOTE: define ‘dialogic’ here in your tool-and-boundary sense, not as ‘more talking’.]",
                    "[ECHO LINE NEEDED: a sentence that calls back to Abraham/Heidi/Nancy or your earlier claim.]",
                ],
            },
            "drag_is_diagnosis": {
                "rule": "Mark drag as a diagnosis, not a rewrite. Bracket and name why it drags so the author can fix it in their own voice.",
                "drag_tags": [
                    "[DRAG: abstract run—needs an anchoring classroom image within 2–3 paragraphs]",
                    "[DRAG: concept introduced twice—choose one home for it]",
                    "[DRAG: too many aspects at once—split into two moves: (1) the problem, (2) dialogism as repair]",
                    "[DRAG: reader lost—needs a micro-signpost: ‘Here’s what I mean…’]",
                ],
            },
            "optional_insert_guardrail": {
                "rule": "Any non-mechanical addition must be wrapped in [OPTIONAL INSERT: …] so nothing sneaks in as ‘yours’.",
            },
            "three_layer_output": [
                "(1) Continuity / structure notes (promise→payoff, terminology, misplaced ideas)",
                "(2) Bracketed missing/drag tags (surgical, non-invasive)",
                "(3) Optional fill choices (2–3 ways you could fill) — choices, not inserted prose",
            ],
            "stripped_draft_rule": {
                "trigger": "If user says ‘do continuity mode / do not add or remove words’.",
                "do": [
                    "Numbered notes only.",
                    "Use brackets in margin-style suggestions, not in-line edits.",
                ],
                "do_not": [
                    "Do not add, remove, or rewrite any words in the draft text.",
                ],
            },
        },
        "passes": [
            {
                "name": "Continuity Mode (Structural Truth Pass — FIRST)",
                "question": "Is the book saying the same thing to itself everywhere?",
                "does": [
                    "Ensure consistent terminology (agency genres, TCS/TSS, shadow of dialogue).",
                    "Check promise → payoff across chapters.",
                    "Protect conceptual boundaries from drift.",
                    "Identify misplaced ideas or overburdened sections.",
                    "Suggest echo lines (intro ↔ later chapters) as placeholders.",
                ],
                "does_not": [
                    "No prose tightening.",
                    "No signposts.",
                    "No stylistic changes.",
                    "Continuity mode diagnoses; it does not cosmetically fix.",
                ],
            },
            {
                "name": "Hampel Tightening + Signposts (Craft Pass — SECOND)",
                "question": "Can the reader stay with me—and remember this?",
                "does": [
                    "Put stories first when they carry the idea.",
                    "Tighten within paragraphs without deleting voice-bearing sections.",
                    "Vary sentence length intentionally; preserve stand-alone sentences for rhythm and moral pressure.",
                    "Remove hedge-stacking and redundancy without thinning the argument.",
                    "Add light, invitational signposts (micro-orientation, bridges, subtle ‘you are here’ cues).",
                ],
                "does_not": [
                    "No meaning changes.",
                    "No tension-resolving.",
                    "No new theory.",
                    "No structural rearranging (that belongs to continuity mode).",
                ],
            },
            {
                "name": "Endnotes & References (Ongoing Hygiene)",
                "question": "Is the grounding present without weighing down the body text?",
                "does": [
                    "Use endnotes for technical terms and research posture / PhD grounding.",
                    "Update references continuously as new chapters are added.",
                    "Chapters 1–3 serve as the locked baseline.",
                ],
            },
        ],
        "chapter_constraints": {
            "Chapter 4": {
                "required_focus": [
                    "Dialogism as necessary to position students as knowers (perceptual footing, reframing, ethical perspectives, testing of ideas)."
                ],
                "prohibited": [
                    "Variation Theory (do not introduce it, reference it, or build explanatory scaffolds around it in Chapter 4)."
                ],
            }
        },
        "memory_anchor": "The contract is always on. Continuity decides where and why. Hampel decides how it lands.",
    }


def to_markdown(c: Dict[str, Any]) -> str:
    lines: List[str] = []

    lines.append(f"# {c['contract_name']} — v{c['version']}")
    lines.append(f"Generated on: {c['generated_on']}")
    lines.append("")
    lines.append(f"**Scope:** {c['scope']}")
    lines.append("")

    lines.append("## Core commitments")
    for k, items in c["core_commitments"].items():
        title = k.replace("_", " ").title()
        lines.append(f"### {title}")
        for item in items:
            lines.append(f"- {item}")
        lines.append("")

    lines.append("## Editing mechanics")
    mech = c["editing_mechanics"]

    lines.append("### No silent fill-in")
    lines.append(f"- {mech['no_silent_fill_in']['rule']}")
    for ex in mech["no_silent_fill_in"]["allowed_placeholders"]:
        lines.append(f"- `{ex}`")
    lines.append("")

    lines.append("### Drag is diagnosis")
    lines.append(f"- {mech['drag_is_diagnosis']['rule']}")
    for ex in mech["drag_is_diagnosis"]["drag_tags"]:
        lines.append(f"- `{ex}`")
    lines.append("")

    lines.append("### Optional insert guardrail")
    lines.append(f"- {mech['optional_insert_guardrail']['rule']}")
    lines.append("")

    lines.append("### Three-layer response")
    for item in mech["three_layer_output"]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("### Stripped draft rule")
    lines.append(f"- **Trigger:** {mech['stripped_draft_rule']['trigger']}")
    lines.append("- **Do:**")
    for item in mech["stripped_draft_rule"]["do"]:
        lines.append(f"  - {item}")
    lines.append("- **Do not:**")
    for item in mech["stripped_draft_rule"]["do_not"]:
        lines.append(f"  - {item}")
    lines.append("")

    lines.append("## Passes")
    for p in c["passes"]:
        lines.append(f"### {p['name']}")
        lines.append(f"**Question:** {p['question']}")
        if "does" in p:
            lines.append("**Does:**")
            for item in p["does"]:
                lines.append(f"- {item}")
        if "does_not" in p:
            lines.append("**Does not:**")
            for item in p["does_not"]:
                lines.append(f"- {item}")
        lines.append("")

    lines.append("## Chapter-specific constraints")
    for ch, spec in c["chapter_constraints"].items():
        lines.append(f"### {ch}")
        lines.append("**Required focus:**")
        for item in spec.get("required_focus", []):
            lines.append(f"- {item}")
        lines.append("**Prohibited:**")
        for item in spec.get("prohibited", []):
            lines.append(f"- {item}")
        lines.append("")

    lines.append("## Memory anchor")
    lines.append(c["memory_anchor"])
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default=".", help="Output directory")
    parser.add_argument("--version", default="2026-01-16", help="Contract version label")
    args = parser.parse_args()

    outdir = Path(args.outdir).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    c = contract(args.version)

    md_path = outdir / "editorial_contract.md"
    json_path = outdir / "editorial_contract.json"

    md_path.write_text(to_markdown(c), encoding="utf-8")
    json_path.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Wrote: {md_path}")
    print(f"Wrote: {json_path}")


if __name__ == "__main__":
    main()
