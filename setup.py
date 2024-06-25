#-*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cc_checker',
    version='0.1.0',
    description='A credit card validator written in Python',
    long_description=readme,
    author='Yannick Tapsoba',
    author_email='53797787+yannick-gst@users.noreply.github.com',
    url='https://github.com/yannick-gst/cc-checker',
    license=license
)
