.PHONY: all python latex clean watch-tex

BUILDDIR := build

all: latex

latex:
	latexmk -pdf -lualatex -synctex=1 -file-line-error -interaction=nonstopmode main.tex -jobname=EENG4312

watch-tex:
	latexmk -pvc -pdf -lualatex -synctex=1 -file-line-error -interaction=nonstopmode main.tex

check: latex
	textidote --output html --check en --remove-macros --ignore sh:seclen,sh:stacked main.tex > $(BUILDDIR)/report.html

clean:
	latexmk -C
	rm -rf build
