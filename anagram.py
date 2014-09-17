__author__ = 'Boh'
#09/16/2014
#problem 1.4
#Q: write a method to decide if two strings are anagram or not

##There is a huge problem in this funcion that i can't figure out why. So anagram('aabc','bbca') gives True
##I've also noticed that whenever I input two strings that have same length, str1dic and str2dic ends up always being the same.
##I don't get dictionary

import copy

def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        strdic = {x: 0 for x in 'abcdefghijklmnoprstuvwxyz '}
        str1dic = copy.copy(strdic)
        str2dic = copy.copy(strdic)
        for i in range(len(str1)):
            str1dic[str1[i]] += 1
            str2dic[str2[i]] += 1
        if str1dic == str2dic:
            return True
        else:
            return False

#Bri's question on this example.
#Q: will it be redundant to create a class in order to check two string? bc i thought of making a class at first.
