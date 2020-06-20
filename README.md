# python-scuttle
Python wrapper around SCUTTLE API.

## Installation

## Usage

Check out the [wiki](https://github.com/scuttle/python-scuttle/wiki/API-v1).

Current SCUTTLE API documentation can be found on [its
wiki](http://scuttle.wikidot.com/api). Most methods are reproduced with similar
names.

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
key in the `SCUTTLE_API_KEY` environment variable. Tests require at least
Python 3.8.
