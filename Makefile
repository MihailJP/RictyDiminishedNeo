TARGETS=RictyDiminishedNeo.ttf RictyDiminishedNeo-Bold.ttf \
RictyDiminishedNeo-Italic.ttf RictyDiminishedNeo-BoldItalic.ttf \
RictyDiminishedNeoDiscord.ttf RictyDiminishedNeoDiscord-Bold.ttf \
RictyDiminishedNeoDiscord-Italic.ttf RictyDiminishedNeoDiscord-BoldItalic.ttf
DOCUMENTS=README.md ChangeLog LICENSE
PACKAGES=RictyDiminishedNeo.tar.xz

.SUFFIXES: .tar.xz

.PHONY: all
all: ${TARGETS}

.INTERMEDIATE: ${TARGETS:.ttf=.ttx} ${TARGETS:.ttf=.raw.ttf} ${TARGETS:.ttf=.raw.ttx}

RictyDiminishedNeo.raw.ttf: Inconsolata-LGC/Inconsolata-LGC.sfd RictyDiminished/RictyDiminished-Regular.ttf SourceHanSans/OTF/Japanese/SourceHanSans-Regular.otf
	./mkfont.py $@ $^

RictyDiminishedNeo-Bold.raw.ttf: Inconsolata-LGC/Inconsolata-LGC-Bold.sfd RictyDiminished/RictyDiminished-Bold.ttf SourceHanSans/OTF/Japanese/SourceHanSans-Bold.otf
	./mkfont.py $@ $^

RictyDiminishedNeo-Italic.raw.ttf: Inconsolata-LGC/Inconsolata-LGC-Italic.sfd RictyDiminished/RictyDiminished-Regular.ttf SourceHanSans/OTF/Japanese/SourceHanSans-Regular.otf
	./mkfont.py $@ $^

RictyDiminishedNeo-BoldItalic.raw.ttf: Inconsolata-LGC/Inconsolata-LGC-BoldItalic.sfd RictyDiminished/RictyDiminished-Bold.ttf SourceHanSans/OTF/Japanese/SourceHanSans-Bold.otf
	./mkfont.py $@ $^

RictyDiminishedNeoDiscord.raw.ttf: Inconsolata-LGC/Inconsolata-LGC.sfd RictyDiminished/RictyDiminishedDiscord-Regular.ttf SourceHanSans/OTF/Japanese/SourceHanSans-Regular.otf
	./mkfont.py $@ $^

RictyDiminishedNeoDiscord-Bold.raw.ttf: Inconsolata-LGC/Inconsolata-LGC-Bold.sfd RictyDiminished/RictyDiminishedDiscord-Bold.ttf SourceHanSans/OTF/Japanese/SourceHanSans-Bold.otf RictyDiminished/RictyDiminishedDiscord-Regular.ttf
	./mkfont.py $@ $^

RictyDiminishedNeoDiscord-Italic.raw.ttf: Inconsolata-LGC/Inconsolata-LGC-Italic.sfd RictyDiminished/RictyDiminishedDiscord-Regular.ttf SourceHanSans/OTF/Japanese/SourceHanSans-Regular.otf
	./mkfont.py $@ $^

RictyDiminishedNeoDiscord-BoldItalic.raw.ttf: Inconsolata-LGC/Inconsolata-LGC-BoldItalic.sfd RictyDiminished/RictyDiminishedDiscord-Bold.ttf SourceHanSans/OTF/Japanese/SourceHanSans-Bold.otf RictyDiminished/RictyDiminishedDiscord-Regular.ttf
	./mkfont.py $@ $^

%.raw.ttx: %.raw.ttf
	ttx -t post -t "OS/2" -o $@ $<
%.ttx: %.raw.ttx
	cat $< | sed -e '/isFixedPitch/s/value=".*"/value="1"/' -e '' -e '/bProportion/s/value=".*"/value="9"/' > $@
%.ttf: %.raw.ttf %.ttx
	ttx -o $@ -m $^

.PHONY: dist
dist: ${PACKAGES}

ChangeLog: .git
	Inconsolata-LGC/mkchglog.rb > $@ # GIT

RictyDiminishedNeo.tar.xz: ${TARGETS} ${DOCUMENTS}
	rm -rf $*; mkdir $*; cp ${TARGETS} ${DOCUMENTS} $*; tar cfvJ $@ $*

.PHONY: clean
clean:
	-rm -f ${TARGETS} ${PACKAGES}
	-rm -f ${TARGETS:.ttf=.ttx} ${TARGETS:.ttf=.raw.ttf} ${TARGETS:.ttf=.raw.ttx}
	-rm -rf ${PACKAGES:.tar.xz=}
