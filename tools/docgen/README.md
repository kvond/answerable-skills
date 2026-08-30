# docgen — the dated Drive accounts

A GitHub repository is not readable the way a Drive folder is, and that is the
whole reason these exist. They render the repository's state into a `.docx` that
lands in `My Drive / Skills Documentation Updates`, where Katherine can open it.

    node doc_github_account.js     # what is in the repository
    node doc_desktop_account.js    # what was on the Desktop and where it went

`build_docs.js` holds the shared typography and table helpers, so a new account
is a list of headings and paragraphs rather than a formatting exercise.

Write a new dated file rather than overwriting the last one. The point of the
folder is the sequence: what the repository looked like on a given date, and
what changed since. An overwritten account answers neither question.

Gotchas that cost time the first run, all from the docx skill: page size
defaults to A4, so US Letter is set explicitly; tables need `columnWidths` on
the table and `width` on every cell, both in DXA; shading must be
`ShadingType.CLEAR`. Column widths must sum to the table width, and a column
narrower than its longest unbreakable word breaks that word mid-way - which is
how "HOLDS" first rendered as "HOLD / S".
