# encoding: utf-8
# Copyright 2009–2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN Miscellaneous Content: test the setup of this package.
'''

import unittest
from edrnsite.misccontent.testing import EDRNSITE_MISC_CONTENT_INTEGRATION_TESTING

class SetupTest(unittest.TestCase):
    '''Unit tests the setup of this package.'''
    layer = EDRNSITE_MISC_CONTENT_INTEGRATION_TESTING
    def setUp(self):
        super(SetupTest, self).setUp()
        self.portal = self.layer['portal']
    # No tests defined at this time.
    

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
