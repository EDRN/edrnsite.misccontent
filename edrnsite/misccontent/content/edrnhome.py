# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN Home.'''

from edrnsite.misccontent.config import PROJECTNAME
from edrnsite.misccontent.interfaces import IEDRNHome
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements
from Products.ATContentTypes.content import document
from edrnsite.misccontent import ProjectMessageFactory as _

EDRNHomeSchema = document.ATDocumentSchema.copy() + atapi.Schema((
    # Nothing else needed.
))
EDRNHomeSchema['title'].storage = atapi.AnnotationStorage()
EDRNHomeSchema['description'].storage = atapi.AnnotationStorage()

finalizeATCTSchema(EDRNHomeSchema, folderish=False, moveDiscussion=False)

class EDRNHome(document.ATDocument):
    '''EDRN Home.'''
    implements(IEDRNHome)
    portal_type               = 'EDRN Home'
    _at_rename_after_creation = True
    schema                    = EDRNHomeSchema
    title                     = atapi.ATFieldProperty('title')
    description               = atapi.ATFieldProperty('description')

atapi.registerType(EDRNHome, PROJECTNAME)
