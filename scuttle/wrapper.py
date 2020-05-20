#!/usr/bin/env python3

"""Provides methods to interface with a given API instance."""

import requests

def scuttle(wiki, api_version=None):
    """Create a new API wrapper for a given wiki and API version.

    str `wiki`: The domain of the wiki.
    int `api_version`: The version of the API to use. If not provided, defaults
    to latest.
    """

