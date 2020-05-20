#!/usr/bin/env python3

import pytest
import scuttle

TOKEN = None
with open("token.secret.txt", 'r') as token_file:
    TOKEN = token_file.readline().strip()

def test_something():
    wiki = scuttle.scuttle('en', 1)
