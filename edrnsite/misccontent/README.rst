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

First we have to set up some things and login to the site::

    >>> app = layer['app']
    >>> from plone.testing.z2 import Browser
    >>> from plone.app.testing import SITE_OWNER_NAME, SITE_OWNER_PASSWORD
    >>> browser = Browser(app)
    >>> browser.handleErrors = False
    >>> browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD))
    >>> portal = layer['portal']    
    >>> portalURL = portal.absolute_url()

Now we can check out the new types introduced in this package.


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
    
