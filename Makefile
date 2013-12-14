SRC=$(wildcard *.tex)
CSV=05_Adressen_Professorenrunde.csv
OUT=$(subst .tex,.pdf,$(SRC))

.PHONY: clean

all: $(OUT)

base.adr: $(CSV)
	@echo create address database ...
	@python csvtoadr.py $< > $@

%.pdf: %.tex base.adr
	@rubber --pdf $<

clean:
	@rubber --clean --pdf $(SRC)
	@rm -f *.out *-blx.bib *.run.xml
