__author__ = 'Boh'
#09/17/2014
#problem 1.5
#Q: Write a method to replace all spaces in a string with '%20'

def replace_to_percent(string_in: str) -> str:
    string_out = ''
    for char in string_in:
        if char == ' ':
            string_out += '%20'
        else:
            string_out += char
    return string_out
