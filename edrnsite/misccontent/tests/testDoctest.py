# encoding: utf-8
# Copyright 2009–2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN Miscellaneous Content: functional and documentation tests.
'''

from edrnsite.misccontent.testing import EDRNSITE_MISC_CONTENT_FUNCTIONAL_TESTING as LAYER
from plone.testing import layered
import doctest
import unittest

optionFlags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE | doctest.REPORT_ONLY_FIRST_FAILURE)

def test_suite():
    return unittest.TestSuite([
        layered(doctest.DocFileSuite('README.rst', package='edrnsite.misccontent', optionflags=optionFlags), LAYER),
    ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
