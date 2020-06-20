try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from scuttle import __version__

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
    install_requires=[
        "requests"
    ]
)
