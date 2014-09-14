__author__ = 'Boh'
#09/14/2014
#Q: Implement an algorithm to determine if a string has all unique characters.
#What if you can not use additional data structures?


def unique_character(x):
    if type(x) != str:
        return False
    else:
        character = [x[0]]
        for i in range(len(x)-1):
            if x[i+1] not in character:
                character.append(x[i+1])
        print(character)
        if len(character) == len(x):
            return True
        else:
            return False
