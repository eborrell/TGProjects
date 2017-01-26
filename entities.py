#!/bin/python

"""
In this script we define the main entities that are involved in the project
"""

from utils import getLowerCamelCase

class Noun(object):
    """
    The noun/sustantive class is defined here.
    A Noun consists of a german term (article + noun) binded to its English translation.

    We must bear in mind that in the dict.cc file, the english translations formed by more than one word are
    described in lower camel case: https://en.wikipedia.org/wiki/Camel_case
    """
    def __init__(self, article, noun, translation):
        self.article = article.lower()
        self.noun = noun.capitalize() #Nouns in german are capitalized
        self.translation = getLowerCamelCase(translation)

    def isMasculine(self):
        return self.article == 'der'

    def isFemenine(self):
        return self.article == 'die'

    def isNeutral(self):
        return self.article == 'das'

class User(object):
    """
    The user class is defined here.

    Each user must have:
      - unique user id (chosen by the user)
      - other interesting attributes?
    """
    def __init__(self, userid):
        self.userid = userid