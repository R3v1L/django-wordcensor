# -*- coding: utf-8 -*-
"""
Django word censoring application administration module
=======================================================

.. module:: 
    :platform: Django
    :synopsis: Django word censoring application administration module
.. moduleauthor:: (C) 2014 Oliver Gutiérrez
"""
# Django imports
from django.contrib import admin

# Application imports
from wordcensor.models import CensoredWord

class CensoredWordAdmin(admin.ModelAdmin):
    """
    CensoredWord administration class
    """
    # Admin parameters    
    
    list_display = ('word','profanity','banned')
    list_filter = ('profanity','banned')
    search_fields = ('word','desc')
    list_editable = ('profanity','banned')
    ordering = ('word',)
    save_on_top = True

# Admin models registration
admin.site.register(CensoredWord, CensoredWordAdmin)
