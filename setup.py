#from distutils.core import setup
from setuptools import setup

setup(
    name='ContactsManager',
    version='1.0',
    packages=['cmcode', 'cmcode.tests'],
    license='Open Source',
    long_description=open('README.txt').read(),
)