TARGETS=RictyDiminishedNeo.ttf RictyDiminishedNeo-Bold.ttf \
RictyDiminishedNeo-Italic.ttf RictyDiminishedNeo-BoldItalic.ttf \
RictyDiminishedNeoDiscord.ttf RictyDiminishedNeoDiscord-Bold.ttf \
RictyDiminishedNeoDiscord-Italic.ttf RictyDiminishedNeoDiscord-BoldItalic.ttf
DOCUMENTS=README.md ChangeLog LICENSE
PACKAGES=RictyDiminishedNeo.tar.xz

.SUFFIXES: .tar.xz

.PHONY: all
all: ${TARGETS}

RictyDiminishedNeo.ttf: Inconsolata-LGC/Inconsolata-LGC.sfd RictyDiminished/RictyDiminished-Regular.ttf
	./mkfont.py $@ $^

RictyDiminishedNeo-Bold.ttf: Inconsolata-LGC/Inconsolata-LGC-Bold.sfd RictyDiminished/RictyDiminished-Bold.ttf
	./mkfont.py $@ $^

RictyDiminishedNeo-Italic.ttf: Inconsolata-LGC/Inconsolata-LGC-Italic.sfd RictyDiminished/RictyDiminished-Regular.ttf
	./mkfont.py $@ $^

RictyDiminishedNeo-BoldItalic.ttf: Inconsolata-LGC/Inconsolata-LGC-BoldItalic.sfd RictyDiminished/RictyDiminished-Bold.ttf
	./mkfont.py $@ $^

RictyDiminishedNeoDiscord.ttf: Inconsolata-LGC/Inconsolata-LGC.sfd RictyDiminished/RictyDiminishedDiscord-Regular.ttf
	./mkfont.py $@ $^

RictyDiminishedNeoDiscord-Bold.ttf: Inconsolata-LGC/Inconsolata-LGC-Bold.sfd RictyDiminished/RictyDiminishedDiscord-Bold.ttf RictyDiminished/RictyDiminishedDiscord-Regular.ttf
	./mkfont.py $@ $^

RictyDiminishedNeoDiscord-Italic.ttf: Inconsolata-LGC/Inconsolata-LGC-Italic.sfd RictyDiminished/RictyDiminishedDiscord-Regular.ttf
	./mkfont.py $@ $^

RictyDiminishedNeoDiscord-BoldItalic.ttf: Inconsolata-LGC/Inconsolata-LGC-BoldItalic.sfd RictyDiminished/RictyDiminishedDiscord-Bold.ttf RictyDiminished/RictyDiminishedDiscord-Regular.ttf
	./mkfont.py $@ $^

.PHONY: dist
dist: ${PACKAGES}

ChangeLog: .git
	Inconsolata-LGC/mkchglog.rb > $@ # GIT

RictyDiminishedNeo.tar.xz: ${TARGETS} ${DOCUMENTS}
	rm -rf $*; mkdir $*; cp ${TARGETS} ${DOCUMENTS} $*; tar cfvJ $@ $*

.PHONY: clean
clean:
	-rm -f ${TARGETS} ${PACKAGES}
	-rm -rf ${PACKAGES:.tar.xz=}
