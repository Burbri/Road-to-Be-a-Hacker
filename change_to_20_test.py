__author__ = 'Boh'

from change_to_20 import *

assert(replace_to_percent('aa b') == 'aa%20b')
assert(replace_to_percent('abc') == 'abc')
assert(replace_to_percent('a b  c d') == 'a%20b%20%20c%20d')

