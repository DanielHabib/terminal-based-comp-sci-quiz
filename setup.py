import os
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path




classifiers=[
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

keywords = [
    "Programming Language :: Python :: 3",    
        ]

packages=find_packages(".")
install_requires=['peppercorn'],


setup(
    name="comp-sci-quiz",
    version="1.0.0",
    description="Terminal Based Computer Science Quiz",
    long_description="A light weight computer science quiz hosted in the terminal",  
    url="https://github.com/DanielHabib/terminal-based-comp-sci-quiz",
    author="Daniel Habib",
    author_email="d.g.habib7@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords=keywords,
    packages=packages,
    install_requires=install_requires,

     
        )
