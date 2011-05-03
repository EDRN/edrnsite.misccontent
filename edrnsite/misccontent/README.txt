==============
 Introduction
==============

This package provides miscellaneous content types for the EDRN public portal.


Installation
============

Add "edrnsite.misccontent" to the buildout.


Content Types
=============

The content types introduced in this package include the following:

EDRN Home
    A customized Page just for the landing of EDRN.

The remainder of this document demonstrates the content types using a series
of functional tests.


Tests
=====

In order to execute these tests, we'll first need a test browser::

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portalURL = self.portal.absolute_url()
        
We also change some settings so that any errors will be reported immediately::

    >>> browser.handleErrors = False
    >>> self.portal.error_log._ignored_exceptions = ()
        
We'll also turn off the portlets.  Why?  Well for these tests we'll be looking
for specific strings output in the HTML, and the portlets will often have
duplicate links that could interfere with that::

    >>> from zope.component import getUtility, getMultiAdapter
    >>> from plone.portlets.interfaces import IPortletManager, IPortletAssignmentMapping
    >>> for colName in ('left', 'right'):
    ...     col = getUtility(IPortletManager, name=u'plone.%scolumn' % colName)
    ...     assignable = getMultiAdapter((self.portal, col), IPortletAssignmentMapping)
    ...     for name in assignable.keys():
    ...             del assignable[name]

And finally we'll log in as an administrator::

    >>> from Products.PloneTestCase.setup import portal_owner, default_password
    >>> browser.open(portalURL + '/login_form?came_from=' + portalURL)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()


Addable Content
---------------

Here we'll exercise some of the content objects available in this project and
demonstrate their properties and constraints.


EDRN Home
~~~~~~~~~

Although it'll typically be added just to the root of the portal (and set as
the default view), an EDRN Home can be instantiated anywhere.  Here, we'll add
it to the root::

    >>> browser.open(portalURL)
    >>> l = browser.getLink(id='edrn-home')
    >>> l.url.endswith('createObject?type_name=EDRN+Home')
    True
    >>> l.click()
    >>> browser.getControl(name='title').value = 'Welcome to EDRN'
    >>> browser.getControl(name='description').value = "You've found the Early Detection Research Network."
    >>> browser.getControl(name='text').value = 'You are most welcome to EDRN.'
    >>> browser.getControl(name='form.button.save').click()
    >>> 'welcome-to-edrn' in portal.objectIds()
    True
    >>> welcome = portal['welcome-to-edrn']
    >>> welcome.title
    'Welcome to EDRN'
    >>> welcome.description
    "You've found the Early Detection Research Network."
    >>> welcome.getText()
    'You are most welcome to EDRN.'
    
