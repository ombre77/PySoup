from lib.pysoup import *


test_style=Style(NamedColor("red"),{TextDecoration.ITALIC:Trilean.TRUE},VanillaFont.DEFAULT)
style_2=Style(font=VanillaFont.ALT)
print(test_style)
print(style_2)
print(test_style+style_2)