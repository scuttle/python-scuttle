#!/usr/bin/env python3

import os
import pytest
import scuttle

API_KEY = os.environ['SCUTTLE_API_KEY']

def test_basic():
    wiki = scuttle.scuttle('en', None, 1)
    assert wiki.domain == 'en'
    assert wiki.version == 1
    assert isinstance(wiki.api, scuttle.versions.v1.Api)

def test_get_nonexistent_version():
    with pytest.raises(ModuleNotFoundError) as e:
        scuttle.scuttle('en', None, 0)
    assert str(e.value) == "API version 0 does not exist."

def test_get_default_version():
    wiki = scuttle.scuttle('en', None)
    assert wiki.version == 1
    assert isinstance(wiki.api, scuttle.versions.v1.Api)

def test_wiki():
    wiki = scuttle.scuttle('en', API_KEY, 1)
    assert wiki.wikis()[0]['subdomain'] == "admin"
    assert wiki.wiki()['subdomain'] == "en"

def test_page():
    wiki = scuttle.scuttle('en', API_KEY, 1)
    pages = wiki.all_pages()
    assert set(pages[0].keys()) == {'id', 'slug', 'wd_page_id'}
    page_id = pages[0]['id']
    assert wiki.page_by_id(page_id)['id'] == page_id
    assert wiki.page_by_slug("scp-1111")['metadata']['wikidot_metadata']['fullname'] == "scp-1111"

def test_revisions():
    wiki = scuttle.scuttle('en', API_KEY, 1)
    page_id = wiki.all_pages()[0]['id']
    revision_id = wiki.page_revisions(page_id)[0]['id']
    assert wiki.get_revision(revision_id)['page_id'] == page_id
    full_revision = wiki.get_full_revision(revision_id)
    assert full_revision['page_id'] == page_id
    assert 'content' in full_revision
