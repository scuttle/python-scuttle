#!/usr/bin/env python3

"""Provides generic methods for accessing version 1 of the API."""

from .base import BaseApi

class Api(BaseApi):
    """API version 1"""
    version = 1

    def wikis(self):
        return self._request("wikis")

    def wiki(self):
        return self._request("wiki")

    def all_pages(self):
        return self._request("page")

    def page_by_id(self, page_id):
        return self._request("page/{}", page_id)

    def page_by_slug(self, page_slug):
        return self._request("page/slug/{}", page_slug)

    def all_page_revisions(self, page_id):
        return self._request("page/{}/revisions", page_id)

    def page_revisions(self, page_id, *, limit=20, offset=0, direction="asc"):
        data = {'limit': limit, 'offset': offset, 'direction': direction}
        return self._request("page/{}/revisions", page_id, data)

    def page_votes(self, page_id):
        return self._request("page/{}/votes", page_id)

    def page_tags(self, page_id):
        return self._request("page/{}/tags", page_id)

    def page_files(self, page_id):
        return self._request("page/{}/files", page_id)

    def get_revision(self, revision_id):
        return self._request("revision/{}", revision_id)

    def get_full_revision(self, revision_id):
        return self._request("revision/{}/full", revision_id)
