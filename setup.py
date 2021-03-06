#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob
from setuptools import setup, find_packages

setup(
    name='argcomplete',
    version='0.3.2',
    url='https://github.com/kislyuk/argcomplete',
    license='Apache Software License',
    author='Andrey Kislyuk',
    author_email='kislyuk@gmail.com',
    description='Bash tab completion for argparse',
    long_description=open('README.rst').read(),
    install_requires=['distribute'],
    packages = find_packages(),
    scripts = glob.glob('scripts/*'),
    package_data={'argcomplete': ['bash_completion.d/python-argcomplete.sh', 'bash_completion/python-setup-py.sh']},
    zip_safe=False,
    include_package_data=True,
    platforms=['MacOS X', 'Posix'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Unix Shell',
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
