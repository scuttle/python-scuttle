#!/usr/bin/env python3

import os
import pytest
import scuttle

TOKEN = os.environ['SCUTTLE_API_KEY']

def test_something():
    wiki = scuttle.scuttle('en', 1)
