#! /usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

from moduleOfRules import __version__ as version

setuptools.setup(
        name='moduleOfRules',
        version=version,
        description='avalição da concepção de um instalador',
        author='LUPS-IoT',
        author_email='trcarvalho@inf.ufpel.edu.br',
        url='https://github.com/hubertokf/lupsEdgeServer',
        packages=['moduleOfRules'],
        license='LUPS-IoT'
)
