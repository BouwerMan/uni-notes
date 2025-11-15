# Course Notes

LaTeX notes for my university classes. Each course lives in its own folder with:

- `main.tex` – entry point
- `tex/` – per-chapter/section/unit notes
- `figures/` – diagrams and plots
- `build/` – latexmk output (ignored)

Build with:

```bash
make
```

All PDFs and LaTeX auxiliary files are treated as build artifacts.
