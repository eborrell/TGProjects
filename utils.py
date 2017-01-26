"""
In this module we define a set of utility functions that might be used throughout
the other modules and don't depend specifically of any particular object.
"""

def isLowerCamelCase(text):
    """Given some text, returns True if the text
    is in lowerCamelCase
    """
    return text[0].islower() and ' ' not in text

def getLowerCamelCase(text):
    """
    Given an english translation in normal notation, transforms it into lower camel case.
    Assumes
    Example: space invaders -> spaceInvaders
    """
    words = text.split(' ')
    if len(words) == 1:
        if isLowerCamelCase(text):
            return text
        else:
            return text.lower()
    else:
        lcamelcase = ''
        for index, word in enumerate(words):
            if index == 0:
                lcamelcase += word.lower()
            else:
                lcamelcase += word.capitalize()
        return lcamelcase


def getNormalCase(self, text):
    """
    Does the opposite of getLowerCamelCase. Given a text in lowerCamelCase,
    returns the text in normal case.
    """
    normalcase = ''
    for letter in text:
        if letter.isupper():
            normalcase += ' ' + letter.lower()
        else:
            normalcase += letter
    return normalcase