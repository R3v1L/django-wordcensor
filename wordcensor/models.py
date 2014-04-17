# -*- coding: utf-8 -*-
"""
Django word censoring application models module
===============================================

.. module:: 
    :platform: Django
    :synopsis: Django word censoring application models module
.. moduleauthor:: (C) 2014 Oliver Gutiérrez
"""

# Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

class CensoredWordManager(models.Manager):
    """
    Censored word manager class
    """
    def as_wordlist(self,**filters):
        """
        Return a word list
        """
        return self.get_queryset().filter(**filters).values_list('word',flat=True)
    
    def get_profanities(self):
        """
        Get profanities word list 
        """
        return self.get_query_set().filter(profanity=True)

    def get_banned(self):
        """
        Get banned word list 
        """
        return self.get_query_set().filter(banned=True)

    def get_profanities_wordlist(self):
        """
        Get profanities word list 
        """
        return self.as_wordlist(profanity=True)

    def get_banned_wordlist(self):
        """
        Get banned word list 
        """
        return self.as_wordlist(banned=True)

class CensoredWord(models.Model):
    """
    Censored word model class
    """
    class Meta:
        """
        Metadata for this model
        """
        verbose_name=_('Censored word')
        verbose_name_plural=_('Censored words')

    created=models.DateTimeField(_('Created'),auto_now_add=True,editable=False,
        help_text=_('Creation date'))
    modified=models.DateTimeField(_('Modified'),auto_now=True,editable=False,
        help_text=_('Modification date'))
    word=models.CharField(_('Word'),max_length=150,
        help_text=_('Censored word'))
    desc=models.TextField(_('Description'),blank=True,null=True,
        help_text=_('Description'))
    profanity=models.BooleanField(_('Profanity'),default=False,
        help_text=_('Specifies if this word should be treated as a profanity'))
    banned=models.BooleanField(_('Banned'),default=False,
        help_text=_('Specifies if this word should be treated as banned'))

    objects=CensoredWordManager()

    def __unicode__(self):
        """
        Model unicode representation
        """
        return self.word
