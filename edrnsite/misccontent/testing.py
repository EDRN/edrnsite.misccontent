# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from plone.app.testing import PloneSandboxLayer, PLONE_FIXTURE, IntegrationTesting, FunctionalTesting
from plone.testing import z2

class EDRNSiteMiscContent(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    def setUpZope(self, app, configurationContext):
        import edrnsite.misccontent
        self.loadZCML(package=edrnsite.misccontent)
        z2.installProduct(app, 'edrnsite.misccontent')
    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'edrnsite.misccontent:default')
    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'edrnsite.misccontent')


EDRNSITE_MISC_CONTENT_FIXTURE = EDRNSiteMiscContent()
EDRNSITE_MISC_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDRNSITE_MISC_CONTENT_FIXTURE,),
    name='EDRNSiteMiscContent:Integration'
)
EDRNSITE_MISC_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDRNSITE_MISC_CONTENT_FIXTURE,),
    name='EDRNSiteMiscContent:Functional'
)
