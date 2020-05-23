#!/usr/bin/env python3

import os
import dateutil.parser as dp

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
    assert wiki.page_by_slug("scp-001")['metadata']['wikidot_metadata']['fullname'] == "scp-001"
    if len(votes := wiki.page_votes(page_id)) > 0:
        assert isinstance(votes[0]['vote'], int)
    if len(tags := wiki.page_tags(page_id)) > 0:
        assert isinstance(tags[0]['name'], str)
    if len(files := wiki.page_files(page_id)) > 0:
        assert isinstance(files[0]['path'], str)


def test_revisions():
    wiki = scuttle.scuttle('en', API_KEY, 1)
    page_id = wiki.all_pages()[0]['id']
    revision_id = wiki.all_page_revisions(page_id)[0]['id']
    assert wiki.get_revision(revision_id)['page_id'] == page_id
    full_revision = wiki.get_full_revision(revision_id)
    assert full_revision['page_id'] == page_id
    assert 'content' in full_revision
    first_rev = wiki.page_revisions(page_id, limit=1, direction="asc")
    assert len(first_rev) == 1
    final_rev = wiki.page_revisions(page_id, limit=1, direction="desc")
    assert dp.parse(first_rev[0]['created_at']) <= dp.parse(final_rev[0]['created_at'])

