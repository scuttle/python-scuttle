#!/usr/bin/env python3

"""Provides generic methods for accessing version 1 of the API."""

from typing import Callable, List, Union

import wrapt

from .base import BaseApi

class NoNonPaginatedVersionError(Exception):
    """Raised when a non-paginated of a paginated-only method is called."""
    pass

@wrapt.decorator
def has_paginated_version(method, instance, args, kwargs):
    def paginated(*args, limit=None, offset=None, direction=None):
        print("PAGINATED METHOD", method)
        print("PAGINATED ARGS", args)
        data = {
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        return method(*args, data=data)
    setattr(instance.verbose, method.__name__, paginated)
    return method

def endpoint(endpoint_url):
    @wrapt.decorator
    def wrapper(method, instance, args, kwargs):
        return instance.request(endpoint_url, *method(*args, **kwargs))
    return wrapper

class PaginatedMethod:
    def __init__(self, method: Callable, verbose_only: bool = False):
        self._method = method
        self._verbose_only = verbose_only

    def __call__(self, *args, **kwargs):
        # Check if this method is only paginated
        # Pop the kwarg first as it must not reach the original method
        if not kwargs.pop('__verbose', False) and self._verbose_only:
            raise NoNonPaginatedVersionError(
                "{} does not have a non-paginated version - use {}.verbose() instead"
            )
        return self._method(*args, **kwargs)

    def verbose(self, *args, limit=None, offset=None, direction=None):
        data = {
            'limit': 20 if limit is None else limit,
            'offset': 0 if offset is None else offset,
            'direction': 'asc' if direction is None else direction,
        }
        return self.__call__(*args, data=data, __verbose=True)

class Api(BaseApi):
    """API version 1"""
    version = 1

    def __init__(self, *args):
        super().__init__(*args)
        self.pages_since = PaginatedMethod(self._pages_since)
        self.page_revisions = PaginatedMethod(self._page_revisions)
        self.forum_threads_since = PaginatedMethod(self._forum_threads_since,
                                                   True)
        self.thread_posts = PaginatedMethod(self._thread_posts)
        self.thread_posts_since = PaginatedMethod(self._thread_posts_since,
                                                  True)
        self.wikidotuser_pages = PaginatedMethod(self._wikidotuser_pages)
        self.wikidotuser_posts = PaginatedMethod(self._wikidotuser_posts)
        self.wikidotuser_revisions = PaginatedMethod(self._wikidotuser_revisions)
        self.tags_pages = PaginatedMethod(self._tags_pages, True)

    @endpoint("wikis")
    def wikis(self):
        return None, None

    @endpoint("wiki")
    def wiki(self):
        return None, None

    @endpoint("page")
    def pages(self):
        return None, None

    @endpoint("page/since/{}")
    def _pages_since(self, since: int, *, data=None):
        if not isinstance(since, int):
            raise TypeError("`since` must be a UNIX timestamp")
        return since, data

    @endpoint("page/{}")
    def page_by_id(self, page_id: int):
        return page_id, None

    @endpoint("page/slug/{}")
    def page_by_slug(self, page_slug: str):
        return page_slug, None

    @endpoint("page/{}/revisions")
    def _page_revisions(self, page_id: int, *, data=None):
        return page_id, data

    @endpoint("page/{}/votes")
    def page_votes(self, page_id):
        return page_id, None

    @endpoint("page/{}/tags")
    def page_tags(self, page_id):
        return page_id, None

    @endpoint("page/{}/files")
    def page_files(self, page_id):
        return page_id, None

    @endpoint("revision/{}")
    def revision(self, revision_id):
        return revision_id, None

    @endpoint("revision/{}/full")
    def full_revision(self, revision_id):
        return revision_id, None

    @endpoint("forum")
    def forums(self):
        return None, None

    @endpoint("forum/{}")
    def forum(self, forum_id):
        return forum_id, None

    @endpoint("forum/{}/threads")
    def forum_threads(self, forum_id):
        return forum_id, None

    @endpoint("forum/{}/since")
    def _forum_threads_since(self, forum_id, since, *, data):
        if not isinstance(since, int):
            raise TypeError("`since` must be a UNIX timestamp")
        data['timestamp'] = since
        return forum_id, data

    @endpoint("thread/{}")
    def thread(self, thread_id):
        return thread_id, None

    @endpoint("thread/{}/posts")
    def _thread_posts(self, thread_id, *, data=None):
        return thread_id, data

    @endpoint("thread/{}/since")
    def _thread_posts_since(self, thread_id, since, *, data):
        if not isinstance(since, int):
            raise TypeError("`since` must be a UNIX timestamp")
        return thread_id, data

    @endpoint("post/{}")
    def post(self, post_id):
        return post_id, None

    @endpoint("post/{}/children")
    def post_children(self, post_id):
        return post_id, None

    @endpoint("post/{}/parent")
    def post_parent(self, post_id):
        return post_id, None

    @endpoint("wikidotuser/{}")
    def wikidotuser(self, user_id: int):
        return user_id, None

    @endpoint("wikidotuser/username/{}")
    def wikidotuser_name(self, wikidot_username: str):
        return wikidot_username, None

    @endpoint("wikidotuser/{}/avatar")
    def wikidotuser_avatar(self, wikidot_user_id: int):
        return wikidot_user_id, None

    @endpoint("wikidotuser/{}/pages")
    def _wikidotuser_pages(self, wikidot_user_id: int, *, data=None):
        if not isinstance(wikidot_user_id, int):
            raise TypeError("Wikidot user ID must be an int")
        return wikidot_user_id, data

    @endpoint("wikidotuser/{}/posts")
    def _wikidotuser_posts(self, wikidot_user_id: int, *, data=None):
        if not isinstance(wikidot_user_id, int):
            raise TypeError("Wikidot user ID must be an int")
        return wikidot_user_id, data

    @endpoint("wikidotuser/{}/revisions")
    def _wikidotuser_revisions(self, wikidot_user_id: int, *, data=None):
        if not isinstance(wikidot_user_id, int):
            raise TypeError("Wikidot user ID must be an int")
        return wikidot_user_id, data

    @endpoint("wikidotuser/{}/votes")
    def wikidotuser_votes(self, wikidot_user_id: int):
        if not isinstance(wikidot_user_id, int):
            raise TypeError("Wikidot user ID must be an int")
        return wikidot_user_id, None

    @endpoint("tag")
    def tags(self):
        return None, None

    @endpoint("tag/{}/pages")
    def tag_pages(self, tag: str):
        """
        str `tag`: One tag, finds page IDs with that tag.
        """
        if not isinstance(tag, str):
            raise TypeError("A single tag must be a string")
        return tag, None

    @endpoint("tag/pages")
    def _tags_pages(self, tags: Union[List[int], List[str]], operator: str = 'and', *, data):
        """
        str[] `tags`: A list of tag names, finds all page IDs that match the
        condition.
        int[] `tags`: A list of SCUTTLE tag IDs, finds all page IDs that match
        the condition.
        str `operator`: 'and' or 'or'; defines the condition when specifying
        multiple tags.
        """
        if isinstance(tags, str):
            raise TypeError("`tags` must be a list of at least one tag; use tag_pages() for a single tag name")
        data['operator'] = operator
        if all(isinstance(tag, str) for tag in tags):
            data['names'] = tags
        elif all(isinstance(tag, int) for tag in tags):
            data['ids'] = tags
        else:
            raise TypeError("`tags` must be a list of str or int")
        return self.request("tag/pages", None, data)
