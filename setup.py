#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# We use calendar versioning
version = "2024.07.24"

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-django",
    version=version,
    description=(
        "A Cookiecutter template for creating production-ready Django projects quickly. Forked from https://github.com/cookiecutter/cookiecutter-django."
    ),
    long_description=long_description,
    author="Enrico Maassa",
    author_email="enrico.massa@gmail.com",
    url="https://github.com/em1208/cookiecutter-django",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, Python, projects, project templates, django, "
        "skeleton, scaffolding, project directory, setup.py"
    ),
)
