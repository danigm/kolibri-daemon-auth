#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

import kolibri_daemon_auth


dist_name = "kolibri_daemon_auth"
# Default description of the distributed package
description = """Kolibri plugin for desktop authentication"""


setup(
    name=dist_name,
    description=description,
    version=kolibri_daemon_auth.__version__,
    author="EndlessOS",
    author_email="danigm@endless.org",
    url="https://github.com/endlessm/kolibri-daemon-auth",
    packages=["kolibri_daemon_auth"],
    entry_points={
        "kolibri.plugins": "kolibri_daemon_auth = kolibri_daemon_auth",
    },
    package_dir={"kolibri_daemon_auth": "kolibri_daemon_auth"},
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords="kolibri",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
