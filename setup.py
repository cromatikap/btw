##
## This file has been written from https://realpython.com/pypi-publish-python-package/#a-small-python-package
##

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "readme.md").read_text()

# This call to setup() does all the work
setup(
    name="btw",
    version="1.0.7",
    description="By The Way is an NLP command line powered by openai",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bidetaggle/btw",
    author="bidetaggle",
    author_email="bidetaggle@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["btw"],
    include_package_data=True,
    install_requires=["wheel", "openai", "toml", "colored", "inquirer"],
    entry_points={
        "console_scripts": [
            "btw=btw.__main__:main",
        ]
    },
)