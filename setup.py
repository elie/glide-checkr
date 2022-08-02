#!/usr/bin/env python


from setuptools import setup

setup(
    name='Glide checkr',
    version='1.5.0',
    description='checkr themes for Glide.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/joelburton/glide-checkr',
    packages=['glide_checkr'],
    install_requires=["glide"],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'revealjs-checkr = glide_checkr',
            'handouts-checkr = glide_checkr',
        ],
    },
)
