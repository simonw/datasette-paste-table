# datasette-paste-table

[![PyPI](https://img.shields.io/pypi/v/datasette-paste-table.svg)](https://pypi.org/project/datasette-paste-table/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-paste-table?include_prereleases&label=changelog)](https://github.com/simonw/datasette-paste-table/releases)
[![Tests](https://github.com/simonw/datasette-paste-table/workflows/Test/badge.svg)](https://github.com/simonw/datasette-paste-table/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-paste-table/blob/main/LICENSE)

Create tables in Datasette by pasting in TSV

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-paste-table

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-paste-table
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
