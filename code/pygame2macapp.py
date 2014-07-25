"""
This is a setup.py script generated by py2applet

Usage:
    python pygame2macapp.py py2app
"""

from setuptools import setup

APP = ['kawax.py']
DATA_FILES = ['img', 'fontzy', 'sound', 'lisezmoi.txt', 'readme.txt']
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)