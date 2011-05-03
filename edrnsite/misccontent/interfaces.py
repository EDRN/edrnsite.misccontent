# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN Miscellaneous Content: interfaces.
'''

from zope import schema
from edrnsite.misccontent import ProjectMessageFactory as _
from Products.ATContentTypes.interface import IATDocument

class IEDRNHome(IATDocument):
    '''EDRN Home.'''
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'Title of this EDRN Home object.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'Brief summary of this EDRN Home object.'),
        required=False,
    )
