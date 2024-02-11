#!/usr/bin/env fontforge -script

from sys import argv
from math import radians
import fontforge, psMat, re

font = fontforge.open(argv[2])
tmpname = font.fontname.replace("InconsolataLGC", "RictyDiminishedNeo")
font.fontname = tmpname
tmpname = font.fullname.replace("Inconsolata LGC", "Ricty Diminished Neo")
font.fullname = tmpname
font.familyname = "Ricty Diminished Neo"
font.em = 1000
font.ascent = 860
font.descent = 140
font.selection.none()
for glyph in font:
	if font[glyph].isWorthOutputting():
		font.selection.select(("more",), glyph)
font.transform(psMat.scale(634/735), ("round",))
font.transform(psMat.translate(-8, 0), ("round",))
for glyph in font.selection.byGlyphs:
	glyph.width = 500
font.copyright = """Copyright (c) 2012-2014 Yasunori Yusa
Copyright (c) 2006 Raph Levien
Copyright (c) 2006-2013 itouhiro
Copyright (c) 2002-2013 M+ FONTS PROJECT
Copyright (c) 2010-2012 Dimosthenis Kaponis
Copyright (c) 2012-2024 MihailJP"""
font.version = "0.1"

ricty = fontforge.open(argv[3])
font.upos = ricty.upos
font.uwidth = ricty.uwidth
font.os2_winascent_add = ricty.os2_winascent_add
font.os2_windescent_add = ricty.os2_windescent_add
font.os2_winascent = ricty.os2_winascent
font.os2_windescent = ricty.os2_windescent
font.os2_typoascent_add = ricty.os2_typoascent_add
font.os2_typodescent_add = ricty.os2_typodescent_add
font.os2_typoascent = ricty.os2_typoascent
font.os2_typodescent = ricty.os2_typodescent
font.os2_typolinegap = ricty.os2_typolinegap
font.hhea_ascent_add = ricty.hhea_ascent_add
font.hhea_descent_add = ricty.hhea_descent_add
font.hhea_ascent = ricty.hhea_ascent
font.hhea_descent = ricty.hhea_descent
font.hhea_linegap = ricty.hhea_linegap
font.os2_family_class = ricty.os2_family_class
font.os2_stylemap = ricty.os2_stylemap
font.os2_panose = ricty.os2_panose
font.os2_version = ricty.os2_version
font.os2_strikeypos = ricty.os2_strikeypos
font.os2_strikeysize = ricty.os2_strikeysize
font.os2_subxoff = ricty.os2_subxoff
font.os2_subxsize = ricty.os2_subxsize
font.os2_subyoff = ricty.os2_subyoff
font.os2_subysize = ricty.os2_subysize
font.os2_supxoff = ricty.os2_supxoff
font.os2_supxsize = ricty.os2_supxsize
font.os2_supyoff = ricty.os2_supyoff
font.os2_supysize = ricty.os2_supysize

if font.italicangle != 0:
	ricty.selection.none()
	for glyph in ricty:
		if ricty[glyph].isWorthOutputting():
			ricty.selection.select(("more",), glyph)
	ricty.transform(psMat.skew(radians(-font.italicangle)), ("round",))

ricty.removeLookup(ricty.gsub_lookups[4])

font.mergeFonts(ricty)
font.encoding = "UnicodeFull"

font.generate(argv[1])
