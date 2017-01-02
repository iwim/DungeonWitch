# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()


with open('LICENSE') as f:
    license = f.read()


setup(
    name='dungeonwitch',
    version='0.0.1',
    description='A PyGame urban witch dungeon crawler',
    long_description=readme,
    author='Briar Rose Schreiber',
    author_email='briarrose@mailbox.org',
    url='https://github.com/GirlVoid/DungeonWitch',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
