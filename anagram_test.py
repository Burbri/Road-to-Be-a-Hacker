__author__ = 'Boh'

from anagram import *

assert(anagram('abcd','abc') == False)
assert(anagam('abc', 'cba') == True)
assert(anagram('aabc','abbc') == False)
assert(unique_character('abcdde', 'dabcde') == True)