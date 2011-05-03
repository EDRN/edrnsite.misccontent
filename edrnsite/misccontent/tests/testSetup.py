# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN Miscellaneous Content: test the setup of this package.
'''

import unittest
from base import BaseTestCase

class TestSetup(BaseTestCase):
    '''Unit tests the setup of this package.'''
    # Nothing at this time
    

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
    
