#!/usr/bin/env python3

"""Provides generic methods for accessing version 1 of the API."""

from .base import BaseApi

class Api(BaseApi):
    """API version 1"""
    version = 1

    def wikis(self):
        return self.request("wikis")
