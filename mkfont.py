#!/usr/bin/env fontforge

from sys import argv
from math import radians
import fontforge, psMat, re

def selectGlyphsWorthOutputting(font, f = lambda _: True):
	font.selection.none()
	for glyph in font:
		if font[glyph].isWorthOutputting() and f(font[glyph]):
			font.selection.select(("more",), glyph)

_, targetFile, ilgcFile, rictyFile, rictyPatchFile, shsansFile, mgenFile, discordFile, *_ = argv + [None] * 8

blockElements = set(range(0x2500, 0x25a0)) \
	| set(range(0x25e2, 0x25e6)) \
	| set(range(0xe0b0, 0xe0b4)) \
	| set(range(0x1fb00, 0x1fbaf))

font = fontforge.open(ilgcFile)
tmpname = font.fontname.replace("InconsolataLGC", "RictyDiminishedNeo")
font.fontname = tmpname
tmpname = font.fullname.replace("Inconsolata LGC", "Ricty Diminished Neo")
font.fullname = tmpname
font.familyname = "Ricty Diminished Neo"
font.em = 1000
font.ascent = 860
font.descent = 140
selectGlyphsWorthOutputting(font, lambda glyph: glyph.unicode not in blockElements)
font.transform(psMat.scale(634/735), ("round",))
font.transform(psMat.translate(-8, 0), ("round",))
selectGlyphsWorthOutputting(font, lambda glyph: glyph.unicode in blockElements)
font.transform(psMat.scale(500/599, 1), ("round",))
font.transform(psMat.translate(0, 40), ("round",))
selectGlyphsWorthOutputting(font)
for glyph in font.selection.byGlyphs:
	glyph.width = 500
font.copyright = """Copyright (c) 2011-2017 Yasunori Yusa
Copyright (c) 2006 Raph Levien
Copyright (c) 2010-2012 Dimosthenis Kaponis
Copyright (c) 2020 itouhiro
Copyright (C) 2002-2019 M+ FONTS PROJECT
Copyright (c) 2012-2024 MihailJP
Copyright 2014-2021 Adobe (http://www.adobe.com/), with Reserved Font Name 'Source'. Source is a trademark of Adobe in the United States and/or other countries.
SIL Open Font License Version 1.1 (http://scripts.sil.org/ofl)"""
font.version = "0.97"
font.sfntRevision = None

ricty = fontforge.open(rictyFile)
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
#font.os2_stylemap = ricty.os2_stylemap
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

shsans = fontforge.open(shsansFile)
makingCache = bool(re.search("SourceHan", targetFile))
tags = {
	"Ideographs": ("jp83", "jp78", "nlck"),
	"Dingbats": (),
	"Generic": (),
	"AlphabeticDigits": (),
	"HDingbats": (),
}

def selectGlyphsWorthOutputting(font):
	font.selection.none()
	for glyph in font:
		if font[glyph].isWorthOutputting():
			font.selection.select(("more",), glyph)

def glyphsWorthOutputting(font):
	for glyph in font:
		if font[glyph].isWorthOutputting():
			yield glyph

def selectCidSubfont(font, subfontname):
	for subfont in range(font.cidsubfontcnt):
		font.cidsubfont = subfont
		if re.search(subfontname, font.fontname):
			break
	else:
		raise ValueError("subfont '" + subfontname + "' not found")

def searchLookup(font, otTag, scriptCode):
	for lookup in font.gsub_lookups:
		for tag, scripts in font.getLookupInfo(lookup)[2]:
			for scr, _ in scripts:
				if tag == otTag and scr == scriptCode:
					return lookup
	return None

font.selection.select("uni233D", "uni2349")
font.unlinkReferences()
rejected_glyphs = set()
for glyph in font:
	if re.search(r'[^v]+circle($|\.)', glyph):
		rejected_glyphs.add(glyph)
	elif re.search(r'\.smallnarrow', glyph):
		rejected_glyphs.add(glyph)
	elif 0x25a0 <= font[glyph].unicode <= 0x25af:
		rejected_glyphs.add(glyph)
	elif 0x25b2 <= font[glyph].unicode <= 0x25cf:
		rejected_glyphs.add(glyph)
	elif 0x2605 <= font[glyph].unicode <= 0x2606:
		rejected_glyphs.add(glyph)
	elif 0x263c <= font[glyph].unicode <= 0x267d:
		rejected_glyphs.add(glyph)
	elif 0x2713 <= font[glyph].unicode <= 0x271d:
		rejected_glyphs.add(glyph)
for glyph in rejected_glyphs:
	font.removeGlyph(glyph)

if not makingCache:
	rejected_glyphs = set()
	for glyph in ricty:
		if 0x2660 <= ricty[glyph].unicode <= 0x2667:
			rejected_glyphs.add(glyph)
		elif 0x2713 <= ricty[glyph].unicode <= 0x271d:
			rejected_glyphs.add(glyph)
	for glyph in rejected_glyphs:
		ricty.removeGlyph(glyph)

	rictyPatch = fontforge.open(rictyPatchFile)
	ricty.mergeFonts(rictyPatch)
	lookup = searchLookup(ricty, 'ccmp', 'kana')
	subtable = ricty.getLookupSubtables(lookup)[0]
	for glyph in glyphsWorthOutputting(ricty):
		if ricty[glyph].color == 0xff00ff:
			glyphPattern = re.search(r'^(uni30[0-9A-F]{2})_(uni309[9A])\.ccmp$', glyph, re.A)
			if glyphPattern:
				print(glyph)
				ricty[glyph].addPosSub(subtable, glyphPattern.group(1, 2))
	rictyPatch.close()
	rictyPatch = None

if font.italicangle != 0:
	selectGlyphsWorthOutputting(ricty)
	ricty.transform(psMat.skew(radians(-font.italicangle)), ("round",))

	for subfont in range(shsans.cidsubfontcnt):
		shsans.cidsubfont = subfont
		selectGlyphsWorthOutputting(shsans)
		shsans.transform(psMat.skew(radians(-font.italicangle)), ("round",))

if re.search('Discord', ricty.fontname):
	tmpname = font.fontname.replace("RictyDiminishedNeo", "RictyDiminishedNeoDiscord")
	font.fontname = tmpname
	tmpname = font.fullname.replace("Ricty Diminished Neo", "Ricty Diminished Neo Discord")
	font.fullname = tmpname
	font.familyname = "Ricty Diminished Neo Discord"

	discord = ricty
	if discordFile:
		discord = fontforge.open(discordFile)

	modified_glyphs = {
		"asterisk", "plus", "comma", "hyphen", "period",
		"zero", "seven", "colon", "semicolon", "less", "equal", "greater",
		"D", "Z", "asciicircum", "z", "bar", "asciitilde",
		# "quotedbl", "quotesingle", "grave",
	}
	if font.italicangle == 0:
		modified_glyphs |= {"l", "r"}
	font.selection.none()
	discord.selection.none()
	for glyph in modified_glyphs:
		font.selection.select(("more",), glyph)
		discord.selection.select(("more",), glyph)
	discord.copy()
	font.paste()
	font.correctDirection()
	if re.search('Bold', font.fontname):
		font.round()
		font.changeWeight(30 * 500 / 613, "LCG", 0, 0.9, "squish")

font.mergeFonts(ricty)
font.encoding = "UnicodeFull"
ricty.close()
ricty = None

# Making cache
if makingCache:
	for subfont in tags.keys():
		selectCidSubfont(shsans, subfont)

		# Rename glyphs, find glyphs already in the target font
		for glyph in glyphsWorthOutputting(shsans):
			if shsans[glyph].glyphname.startswith('Identity') and shsans[glyph].unicode >= 0:
				newName = ""
				if shsans[glyph].unicode in font and font[shsans[glyph].unicode].isWorthOutputting():
					shsans[glyph].color = 0xffff00
					newName = font[shsans[glyph].unicode].glyphname
				else:
					shsans[glyph].color = 0x00ffff
					newName = fontforge.nameFromUnicode(shsans[glyph].unicode)
				print("Rename glyph '{0}' -> '{1}'".format(glyph, newName))
				shsans[glyph].glyphname = newName
				if subfont == "Ideographs":
					for lookup in shsans[newName].getPosSub("*"):
						if lookup[0].startswith("'jp90'"):
							if lookup[2].startswith('Identity'):
								if (newName + ".jp90") in font:
									shsans[lookup[2]].color = 0xffff00
								else:
									shsans[lookup[2]].color = 0x00ffff
								print("Rename glyph '{0}' -> '{1}.jp90'".format(lookup[2], newName))
								shsans[lookup[2]].glyphname = newName + "." + tag
				for tag in ("jp83", "jp78", "nlck"):
					for lookup in shsans[newName].getPosSub("*"):
						if lookup[0].startswith("'" + tag + "'"):
							if lookup[2] in shsans and lookup[2].startswith('Identity') and shsans[lookup[2]].unicode == -1:
								print("Rename glyph '{0}' -> '{1}.{2}'".format(lookup[2], newName, tag))
								shsans[lookup[2]].color = 0x00ffff
								shsans[lookup[2]].glyphname = newName + "." + tag
			elif shsans[glyph].glyphname.startswith('Identity') and shsans[glyph].altuni:
				for altUniVal, variationSelector, reserved in shsans[glyph].altuni:
					if variationSelector >= 0:
						newName = fontforge.nameFromUnicode(altUniVal) + "_" + fontforge.nameFromUnicode(variationSelector)
						print("Rename glyph '{0}' -> '{1}'".format(glyph, newName))
						shsans[glyph].color = 0x00ffff
						shsans[glyph].glyphname = newName
						break

		# Remove unneeded glyphs
		rejected_glyphs = []
		for glyph in shsans:
			if glyph.startswith('Identity'):
				rejected_glyphs += [glyph]
		for glyph in rejected_glyphs:
			print("Removing glyph '{0}'".format(glyph))
			shsans.removeGlyph(glyph)

		# Output
		shsans.save(targetFile)

# Making font
else:
	for subfont in tags.keys():
		selectCidSubfont(shsans, subfont)

		# Merge Source Han Sans
		selectGlyphsWorthOutputting(shsans)
		shsans.transform(psMat.compose(psMat.scale(0.91), psMat.translate(23, 0)), ('noWidth', 'round'))
		font.mergeFonts(shsans)
		font.encoding = "UnicodeFull"

	# Remove unneeded lookups
	for lookup in font.gsub_lookups:
		if re.search("'aalt'", lookup) or lookup.startswith(shsans.cidfontname + "-'locl'"):
			font.removeLookup(lookup)

	# Add missing entries into 'jp83' and 'jp78' lookup tables
	shsans.cidFlatten()
	for tag in tags["Ideographs"]:
		for lookup in font.gsub_lookups:
			if re.search("-'" + tag + "'", lookup):
				font.removeLookup(lookup)
		for lookup in shsans.gsub_lookups:
			if re.search("'" + tag + "'", lookup):
				font.importLookups(shsans, lookup)

	shsans.close()
	shsans = None

	# Merge Mgen+
	mgen = fontforge.open(mgenFile)
	mgen.em = 1000
	mgen.ascent = 860
	mgen.descent = 140
	selectGlyphsWorthOutputting(mgen)
	mgen.transform(psMat.compose(psMat.scale(0.91), psMat.translate(23, 0)), ('noWidth', 'round'))
	if font.italicangle != 0:
		selectGlyphsWorthOutputting(mgen)
		mgen.transform(psMat.skew(radians(-font.italicangle)), ("round",))
	font.mergeFonts(mgen)
	font.encoding = "UnicodeFull"
	mgen.close()
	mgen = None

	# Update `aalt` feature
	font.buildOrReplaceAALTFeatures()

	# Output
	font.generate(targetFile)
