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

def test_pagination():
    wiki = scuttle.scuttle('en', API_KEY, 1)
    # will be testing on page revisions pagination
    page_slug = "main"
    page_id = wiki.page_by_slug(page_slug)['id']
    # non-paginated revisions - should just be metadata
    print("DOING non-paginated")
    non_paginated_revisions = wiki.all_pagerevisions(page_id)
    print("DONE non-paginated")
    assert len(non_paginated_revisions) > 100
    assert 'content' not in non_paginated_revisions[0].keys()
    # paginated revisions - should include revision content
    print("DOING paginated")
    paginated_revisions = wiki.all_pagerevisions.verbose(page_id)
    print("DONE paginated")
    assert 'content' in paginated_revisions[0].keys()
    assert len(paginated_revisions) == 20

def test_page():
    wiki = scuttle.scuttle('en', API_KEY, 1)
    pages = wiki.all_pages()
    assert set(pages[0].keys()) == {'id', 'slug', 'wd_page_id'}
    page_id = pages[0]['id']
    assert wiki.page_by_id(page_id)['id'] == page_id
    assert wiki.page_by_slug("scp-001")['metadata']['wikidot_metadata']['fullname'] == "scp-001"
    assert wiki.page_by_slug("component:ar-theme")['metadata']['wikidot_metadata']['created_by'] == "Croquembouche"
    if len(votes := wiki.page_votes(page_id)) > 0:
        assert isinstance(votes[0]['vote'], int)
    if len(tags := wiki.page_tags(page_id)) > 0:
        assert isinstance(tags[0]['name'], str)
    if len(files := wiki.page_files(page_id)) > 0:
        assert isinstance(files[0]['path'], str)
    timestamp = 1500000000
    pages_since_then = wiki.all_pages_since_mini(timestamp)
    print(pages_since_then)
    assert all(page['metadata']['wd_page_created_at'] >= timestamp
               for page in pages_since_then)

def test_revisions():
    wiki = scuttle.scuttle('en', API_KEY, 1)
    page_id = wiki.all_pages()[0]['id']
    print(f"{page_id=}")
    revision_id = wiki.all_page_revisions(page_id)[0]['id']
    print(f"{revision_id=}")
    assert wiki.get_revision(revision_id)['page_id'] == page_id
    full_revision = wiki.get_full_revision(revision_id)
    print(f"{full_revision=}")
    assert full_revision['page_id'] == page_id
    assert 'content' in full_revision
    first_rev = wiki.page_revisions(page_id, limit=1, direction="asc")
    print(f"{first_rev=}")
    assert len(first_rev) == 1
    final_rev = wiki.page_revisions(page_id, limit=1, direction="desc")
    print(f"{final_rev=}")
    assert first_rev[0]['metadata']['wikidot_metadata']['timestamp'] <= final_rev[0]['metadata']['wikidot_metadata']['timestamp']

def test_forums():
    wiki = scuttle.scuttle('en', API_KEY, 1)
    forum_id = wiki.all_forums()[0]['id']
    assert wiki.forum(forum_id)['id'] == forum_id

def test_tags():
    # TODO
    pass
