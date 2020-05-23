#!/usr/bin/env python3

"""Provides generic methods for accessing version 1 of the API."""

from .base import BaseApi

class Api(BaseApi):
    """API version 1"""
    version = 1

    def wikis(self):
        return self.request("wikis")

    def wiki(self):
        return self.request("wiki")

    def all_pages(self):
        return self.request("page")

    def page_by_id(self, page_id):
        return self.request("page/{}", page_id)

    def page_by_slug(self, page_slug):
        return self.request("page/slug/{}", page_slug)

    def page_revisions(self, page_id):
        return self.request("page/{}/revisions", page_id)

    def get_revision(self, revision_id):
        return self.request("revision/{}", revision_id)

    def get_full_revision(self, revision_id):
        return self.request("revision/{}/full", revision_id)
