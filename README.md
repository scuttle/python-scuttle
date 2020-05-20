# python-scuttle
Python wrapper around SCUTTLE API.

## Installation

## Usage

## Testing

Install [Pipenv](https://pypi.org/project/pipenv/) and install development
dependencies:

```shell
pipenv install --dev
```

Run tests in pipenv environment:

```shell
pipenv run pytest
```

Tests require a SCUTTLE API key with full permissions. This key should be the
contents of `token.secret.txt` which is to be placed in the test directory. Do
make sure it's in the gitignore.
