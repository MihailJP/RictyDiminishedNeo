TARGETS=RictyDiminishedNeo.ttf RictyDiminishedNeo-Bold.ttf RictyDiminishedNeo-Italic.ttf RictyDiminishedNeo-BoldItalic.ttf

.PHONY: all
all: $(TARGETS)

RictyDiminishedNeo.ttf: Inconsolata-LGC/Inconsolata-LGC.sfd RictyDiminished/RictyDiminished-Regular.ttf
	./mkfont.py $@ $^

RictyDiminishedNeo-Bold.ttf: Inconsolata-LGC/Inconsolata-LGC-Bold.sfd RictyDiminished/RictyDiminished-Bold.ttf
	./mkfont.py $@ $^

RictyDiminishedNeo-Italic.ttf: Inconsolata-LGC/Inconsolata-LGC-Italic.sfd RictyDiminished/RictyDiminished-Regular.ttf
	./mkfont.py $@ $^

RictyDiminishedNeo-BoldItalic.ttf: Inconsolata-LGC/Inconsolata-LGC-BoldItalic.sfd RictyDiminished/RictyDiminished-Bold.ttf
	./mkfont.py $@ $^

.PHONY: clean
clean:
	-rm -f $(TARGETS)
