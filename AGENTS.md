# Workspace Instructions

## Project Structure
- `main.tex` is the root LaTeX document.
- `bib.tex` contains BibTeX entries. Preserve citation keys and BibTeX field structure when editing it.
- Generated files such as `.aux`, `.bbl`, `.fdb_latexmk`, `.fls`, `.log`, `.out`, `.pdf`, `.synctex.gz`, and `.toc` are build artifacts; do not edit them by hand.

## LaTeX Conventions
- Preserve the existing `article` document class, package choices, and `natbib` numerical, sorted, compressed citation style unless asked to change them.
- Keep wide or multi-page data tables in the existing `longtable` style, using `booktabs` rules where appropriate.
- Escape LaTeX-special characters in table text and maintain consistent column alignment and row endings.
- Keep edits focused; do not reformat large data tables or bibliography entries unnecessarily.

## Build and Validation
- The workspace contains `latexmk` build artifacts; use `latexmk -pdf main.tex` when `latexmk` is available.
- Resolve LaTeX errors and bibliography warnings from the build output. Do not treat a stale generated PDF or auxiliary file as source.
- `main.tex` currently requests `references` via `\bibliography{references}`, while the visible bibliography source is `bib.tex`. Check and reconcile the bibliography basename before changing bibliography-related build behavior.
