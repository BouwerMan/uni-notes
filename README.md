# Notes

[![Build LaTeX Notes](https://github.com/BouwerMan/uni-notes/actions/workflows/build-notes.yml/badge.svg)](https://github.com/BouwerMan/uni-notes/actions/workflows/build-notes.yml)

Automatically compiled LaTeX notes for my university classes, plus textbook-style
reference books for engineering projects I'm working on.

A live version of all compiled PDFs is available here:
**<https://bouwerman.github.io/uni-notes/>**

---

## Courses

| Course Code | Description           | PDF Link                                                       |
| ----------- | --------------------- | -------------------------------------------------------------- |
| EENG 4312   | Communications Theory | [View PDF](https://bouwerman.github.io/uni-notes/EENG4312.pdf) |

## Reference

| Folder      | Description                                          | PDF Link                                                        |
| ----------- | ---------------------------------------------------- | --------------------------------------------------------------- |
| EMIFilter   | EMI input filter design for DC-DC converters         | [View PDF](https://bouwerman.github.io/uni-notes/EMIFilter.pdf) |

---

## Structure

Each course or reference book lives in its own folder with the following layout:

- `main.tex` – entry point
- `tex/` – per-chapter or unit notes
- `figures/` – diagrams and plots
- `scripts/` – optional scripts that generate figure data (output is committed)
- `build/` – latexmk output (ignored in git)

Course folders are listed in `CLASSES` and reference books in `REFERENCE` in the
root `Makefile`. All PDFs are collected and published automatically via GitHub Actions and GitHub Pages.

---

## Building locally

To compile everything:

```bash
make
```

This produces a site/ directory with:

- one PDF per course or reference book
- a generated HTML index page
- content identical to what is published on GitHub Pages

## Notes

- All PDFs and LaTeX auxiliary files are treated strictly as build artifacts.
- These notes are for personal study and reference — correctness is not guaranteed.
- Built using LaTeX, Make, and GitHub Actions.
