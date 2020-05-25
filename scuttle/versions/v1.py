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

    def page_revisions(self, page_id, *,
                       limit, offset, direction):
        data = {
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
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

    def all_forums(self):
        return self._request("forum")

    def forum(self, forum_id):
        return self._request("forum/{}", forum_id)

    def forum_threads(self, forum_id):
        return self._request("forum/{}/threads", forum_id)

    def forum_threads_since(self, forum_id, since, *,
                            limit, offset, direction):
        if not isinstance(since, int):
            raise TypeError("`since` must be a UNIX timestamp")
        data = {
            'timestamp': since,
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        return self._request("forum/{}/since", forum_id, data)

    def thread(self, thread_id):
        return self._request("thread/{}", thread_id)

    def all_thread_posts(self, thread_id):
        return self._request("thread/{}/posts", thread_id)

    def thread_posts(self, thread_id, *,
                     limit, offset, direction):
        data = {
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        return self._request("thread/{}/posts", thread_id, data)

    def thread_posts_since(self, thread_id, since, *,
                           limit, offset, direction):
        if isinstance(since, int):
            data = {
                'timestamp': since,
                'limit': 20 if limit is None else limit,
                'offset': 0 if offset is None else offset,
                'direction': 'asc' if direction is None else direction,
            }
            return self._request("thread/{}/since", thread_id, data)
        raise TypeError("`since` must be a UNIX timestamp")

    def post(self, post_id):
        return self._request("post/{}", post_id)

    def post_children(self, post_id):
        return self._request("post/{}/children", post_id)

    def post_parent(self, post_id):
        return self._request("post/{}/parent", post_id)

    def wikidotuser(self, wikidotuser_id):
        return self._request("wikidotuser/{}", wikidotuser_id) # TODO typecheck
        return self._request("wikidotuser/username/{}", wikidotuser_id)

    def wikidotuser_avatar(self, wikidotuser_id):
        return self._request("wikidotuser/{}/avatar", wikidotuser_id)

    def wikidotuser_pages(self, wikidotuser_id):
        return self._request("wikidotuser/{}/pages", wikidotuser_id) # TODO POST

    def wikidotuser_posts(self, wikidotuser_id):
        return self._request("wikidotuser/{}/posts", wikidotuser_id) # TODO POST

    def wikidotuser_revisions(self, wikidotuser_id):
        return self._request("wikidotuser/{}/revisions", wikidotuser_id) # TODO POST

    def wikidotuser_votes(self, wikidotuser_id):
        return self._request("wikidotuser/{}/votes", wikidotuser_id)

    def tags(self):
        return self._request("tag")

    def tag(self, tag_name):
        return self._request("tag/{}/pages", tag_name) # TODO allow POST and ids and stuff


