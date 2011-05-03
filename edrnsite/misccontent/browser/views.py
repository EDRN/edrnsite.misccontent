# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN Miscellaneous Content: views for content types.
'''

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class EDRNHomeView(BrowserView):
    '''Default view for an EDRN Home.'''
    __call__ = ViewPageTemplateFile('templates/edrnhome.pt')
