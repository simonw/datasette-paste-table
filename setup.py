from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-paste-table",
    description="Create tables in Datasette by pasting in TSV",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-paste-table",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-paste-table/issues",
        "CI": "https://github.com/simonw/datasette-paste-table/actions",
        "Changelog": "https://github.com/simonw/datasette-paste-table/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_paste_table"],
    entry_points={"datasette": ["paste_table = datasette_paste_table"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
