import fontforge
import sys

font = fontforge.font()
glyph = font.createChar(58352, "font1")
glyph.importOutlines("AsahiLinux_logomark.svg")
font.generate("../src/glyphs/asahi.otf")

print("Test the font:")
sys.stdout.buffer.write("\ue3f0".encode("utf-8"))
