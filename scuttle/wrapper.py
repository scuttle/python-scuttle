#!/usr/bin/env python3

"""Provides methods to interface with a given API instance."""

import requests
import importlib

print(importlib.import_module('.v1', 'scuttle.versions'))

def scuttle(wiki, api_key, api_version=1):
    """Create a new API wrapper for a given wiki and API version.

    str `wiki`: The domain of the wiki.
    str `api_key`: Your SCUTTLE API key.
    int `api_version`: The version of the API to use. If not provided, defaults
    to 1.
    """
    if api_version is None:
        raise NotImplementedError
    return ApiWrapper(wiki, api_key, api_version)

class ApiWrapper:
    def __init__(self, wiki, api_key, api_version):
        self.domain = wiki
        self.api_key = api_key
        self.version = api_version

        try:
            api_module = importlib.import_module(".v{}".format(self.version),
                                                 'scuttle.versions')
        except ModuleNotFoundError:
            raise ModuleNotFoundError("API version {} does not exist."
                                      .format(self.version))
        self.api = api_module.Api(self.domain, self.api_key)

    def __getattr__(self, attr):
        # Redirect attribute requests to api.
        # Where no such property exists, raise a verbose error.
        return getattr(self.api, attr)
