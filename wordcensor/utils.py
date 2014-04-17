# -*- coding: utf-8 -*-
"""
Django word censoring application utilities module
===============================================

.. module:: 
    :platform: Django
    :synopsis: Django word censoring application utilities module
.. moduleauthor:: (C) 2014 Oliver Gutiérrez
"""

# Python imports
import string

# Django imports
from django.conf import settings

# Application imports
from wordcensor.models import CensoredWord

def profanity_word_handler(word):
    """
    Returns a word censored 
    """
    return word[0] + ''.join([settings.CENSOR_PROFANITY_REPLACEMENT_CHARACTER for I in range(len(word)-2)]) + word [-1]

def banned_word_handler(word):
    """
    Returns a word totally replaced by a character 
    """
    return ''.join([settings.CENSOR_BANNED_REPLACEMENT_CHARACTER for x in word])

def word_filter(text,wordlist,replace_handler,separator=' '):
    """
    Generic word filter
    """
    for word in wordlist:
        if word in text:
            try:
                replacement=replace_handler(word)
            except Exception, e:
                print e
                replacement=replace_handler
            text=text.replace(word,replacement)
    return text
    
def filter_profanities(text,replace_handler=profanity_word_handler):
    """
    Replaces profanities in a given text
    """
    profanities=CensoredWord.objects.get_profanities_wordlist()
    return word_filter(text,profanities,replace_handler)
    
def filter_banned(text,replace_handler=banned_word_handler):
    """
    Replaces banned in a given text
    """
    banned=CensoredWord.objects.get_banned_wordlist()
    return word_filter(text,banned,replace_handler)