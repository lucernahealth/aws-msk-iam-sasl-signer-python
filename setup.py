#!/usr/bin/env python

#  Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

"""The setup script."""

from distutils.core import setup

from setuptools import find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.rst") as changelog_file:
    history = changelog_file.read()

# Do not touch without good reason! These versions are pinned to be
# compatible with Glue 3.0
requirements = ["boto3==1.18.65", "botocore==1.21.65"]

test_requirements = [
    "pytest==7.3.1",
    "pytest-cov==4.0.0",
    "coverage==7.2.5",
    "mock==5.0.2",
]

setup(
    author="Amazon Managed Streaming for Apache Kafka",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description="Amazon MSK Library in Python for SASL/OAUTHBEARER Auth",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description_content_type="text/x-rst",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="aws-msk-iam-sasl-signer-python",
    name="aws-msk-iam-sasl-signer-python",
    packages=find_packages(exclude=['tests*']),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/aws/aws-msk-iam-sasl-signer-python",
    version="1.0.1",
    zip_safe=False,
)
