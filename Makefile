# KnowhutImean?
TARGET = mss
BIBFILE = ernest

all: $(TARGET).pdf

$(TARGET).pdf: $(TARGET).tex $(BIBFILE).bib
	xelatex -interaction=nonstopmode $(TARGET)
	bibtex $(TARGET)
	xelatex -interaction=nonstopmode $(TARGET)
	xelatex -interaction=nonstopmode $(TARGET)

clean:
	rm -f $(TARGET).pdf *.aux *.bbl *.blg *.log *.out *.toc

.PHONY: all clean
