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
        wiki = scuttle.scuttle('en', None, 0)
    assert str(e.value) == "API version 0 does not exist."

def test_get_default_version():
    wiki = scuttle.scuttle('en', None)
    assert wiki.version == 1
    assert isinstance(wiki.api, scuttle.versions.v1.Api)

def test_get_wikis():
    wiki = scuttle.scuttle('en', API_KEY, 1)
    print(wiki.wikis())
    assert False
