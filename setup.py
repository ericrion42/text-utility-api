"""
setup.py

Minimal setup script for backward compatibility with older tooling.
Modern packaging metadata lives in pyproject.toml; this file exists
because many tools and tutorials still expect to see it.
"""

from setuptools import setup, find_packages

setup(
    name="text-utils-pkg",
    version="1.0.0",
    packages=find_packages(),
)