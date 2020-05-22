# python-scuttle
Python wrapper around SCUTTLE API.

## Installation

## Usage

Create a wrapper for a given wiki and API version:

```python
from scuttle import scuttle

wiki = scuttle('en', 1)
```

## Testing

Install [Pipenv](https://pypi.org/project/pipenv/) and install development
dependencies:

```shell
pipenv install --dev
```

Run tests in pipenv environment:

```shell
pipenv run python3 -m pytest
```

Tests require a SCUTTLE API key with full permissions. Tests will look for this
key in the `SCUTTLE_API_KEY` environment variable.
