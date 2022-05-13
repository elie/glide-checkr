#!/usr/bin/env python


from setuptools import setup

setup(
    name='Glide walmart',
    version='1.5.0',
    description='walmart themes for Glide.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/joelburton/glide-walmart',
    packages=['glide_walmart'],
    install_requires=["glide"],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'revealjs-walmart = glide_walmart',
            'handouts-walmart = glide_walmart',
        ],
    },
)
