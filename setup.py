from distutils.core import setup
import setuptools
import py2exe

setup(
    console = [{'script': 'ono.py'}] # exe化するファイル
)