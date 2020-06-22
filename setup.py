try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from scuttle import __version__

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scuttle',
    version=__version__,
    packages=[
        'scuttle',
        'scuttle.versions'
    ],
    url="http://github.com/scuttle/python-scuttle",
    license="MIT",
    author="Ross Williams",
    author_email="ross@rossjrw.com",
    description="Python wrapper for SCUTTLE API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "requests"
    ]
)
