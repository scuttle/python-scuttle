#!/usr/bin/env python3

"""Provides generic methods for accessing version 1 of the API."""

from collections.abc import Iterable

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
                       limit=None, offset=None, direction=None):
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
                            limit=None, offset=None, direction=None):
        data = {
            'timestamp': since,
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        if not isinstance(since, int):
            raise TypeError("`since` must be a UNIX timestamp")
        return self._request("forum/{}/since", forum_id, data)

    def thread(self, thread_id):
        return self._request("thread/{}", thread_id)

    def all_thread_posts(self, thread_id):
        return self._request("thread/{}/posts", thread_id)

    def thread_posts(self, thread_id, *,
                     limit=None, offset=None, direction=None):
        data = {
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        return self._request("thread/{}/posts", thread_id, data)

    def thread_posts_since(self, thread_id, since, *,
                           limit=None, offset=None, direction=None):
        data = {
            'timestamp': since,
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        if not isinstance(since, int):
            raise TypeError("`since` must be a UNIX timestamp")
        return self._request("thread/{}/since", thread_id, data)

    def post(self, post_id):
        return self._request("post/{}", post_id)

    def post_children(self, post_id):
        return self._request("post/{}/children", post_id)

    def post_parent(self, post_id):
        return self._request("post/{}/parent", post_id)

    def wikidotuser(self, wikidotuser_id):
        if isinstance(wikidotuser_id, int):
            return self._request("wikidotuser/{}", wikidotuser_id)
        return self._request("wikidotuser/username/{}", wikidotuser_id)

    def wikidotuser_avatar(self, wikidotuser_id):
        if not isinstance(wikidotuser_id, int):
            raise TypeError("The Wikidot user ID must be an int")
        return self._request("wikidotuser/{}/avatar", wikidotuser_id)

    def all_wikidotuser_pages(self, wikidotuser_id):
        if not isinstance(wikidotuser_id, int):
            raise TypeError("The Wikidot user ID must be an int")
        return self._request("wikidotuser/{}/pages", wikidotuser_id)

    def wikidotuser_pages(self, wikidotuser_id, *,
                          limit=None, offset=None, direction=None):
        data = {
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        if not isinstance(wikidotuser_id, int):
            raise TypeError("The Wikidot user ID must be an int")
        return self._request("wikidotuser/{}/pages", wikidotuser_id, data)

    def all_wikidotuser_posts(self, wikidotuser_id):
        if not isinstance(wikidotuser_id, int):
            raise TypeError("The Wikidot user ID must be an int")
        return self._request("wikidotuser/{}/posts", wikidotuser_id)

    def wikidotuser_posts(self, wikidotuser_id, *,
                          limit=None, offset=None, direction=None):
        data = {
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        if not isinstance(wikidotuser_id, int):
            raise TypeError("The Wikidot user ID must be an int")
        return self._request("wikidotuser/{}/posts", wikidotuser_id, data)

    def all_wikidotuser_revisions(self, wikidotuser_id):
        if not isinstance(wikidotuser_id, int):
            raise TypeError("The Wikidot user ID must be an int")
        return self._request("wikidotuser/{}/revisions", wikidotuser_id)

    def wikidotuser_revisions(self, wikidotuser_id, *,
                              limit=None, offset=None, direction=None):
        data = {
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        if not isinstance(wikidotuser_id, int):
            raise TypeError("The Wikidot user ID must be an int")
        return self._request("wikidotuser/{}/revisions", wikidotuser_id, data)

    def wikidotuser_votes(self, wikidotuser_id):
        if not isinstance(wikidotuser_id, int):
            raise TypeError("The Wikidot user ID must be an int")
        return self._request("wikidotuser/{}/votes", wikidotuser_id)

    def tags(self):
        return self._request("tag")

    def tag_pages(self, tags):
        """
        str `tags`: One tag, finds page IDs with that tag.
        """
        if not isinstance(tags, str):
            raise TypeError("A single tag must be a string")
        return self._request("tag/{}/pages", tags)

    def tags_pages(self, tags, operator='and', *,
                   limit=None, offset=None, direction=None):
        """
        str[] `tags`: A list of tags, finds all page IDs that match the
        condition.
        int[] `tags`: A list of SCUTTLE tag IDs, finds all page IDs that match
        the condition.
        str `operator`: 'and' or 'or'; defines the condition when specifying
        multiple tags.
        """
        if isinstance(tags, str):
            raise TypeError("tags must be str[] or int[]; use tag_pages()"
                            "for single tags")
        if not isinstance(tags, Iterable):
            raise TypeError("tags must be a list of str or int")
        data = {
            'operator': operator,
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        if all(isinstance(tag, str) for tag in tags):
            data.update({'names': tags})
            return self._request("tag/pages", None, data)
        if all(isinstance(tag, int) for tag in tags):
            data.update({'ids': tags})
            return self._request("tag/pages", None, data)
        raise TypeError("tags must be a list of str or int")
