#!/usr/bin/python3
"""
Function that prints a text with 2 ines after special chars
python3 -c 'print(__import__("my_module").__doc__)'
"""


def text_indentation(text):
    """
    text_indentation - function that prints text lines after special chars
    text: text to test
    Retrun: nothing
    python3 -c 'print(__import__("my_module").__doc__)'
    """
    flag = [".", "?", ":"]
    if isinstance(text, str) is False:
        raise TypeError("text must be a sting")
    after_newline = False
    for c in text:
        if after_newline:
            if c == " ":
                continue
            after_newline = False
        if c in flag:
            print(c)
            print()
            after_newline = True
        else:
            print(c, end="")
