##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup

$Id:$
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup (
    name='z3c.language.negotiator',
    version='1.1.4dev',
    author = "Roger Ineichen and the Zope Community",
    author_email = "zope-dev@zope.org",
    description = "Zope3 i18n language negotiator.",
    long_description=(
        read('README.txt')
        + '\n\n' +
        'Detailed Documentation\n'
        '**********************'
        + '\n\n' +
        read('src', 'z3c', 'language', 'negotiator', 'README.txt')
        + '\n\n' +
        read('CHANGES.txt')
        ),
    license = "ZPL 2.1",
    keywords = "zope3 z3c i18n language negotiator",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope :: 3'],
    url = 'http://pypi.python.org/pypi/z3c.language.negotiator',
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['z3c', 'z3c.language'],
    extras_require = dict(
        test = [
            'z3c.testing',
            'z3c.coverage',
            'zope.testing',
            ],
        ),
    install_requires = [
        'setuptools',
        'z3c.language.session',
        'zope.app.generations',
        'zope.component',
        'zope.container',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.publisher',
        'zope.schema',
        ],
    zip_safe = False,
    )
