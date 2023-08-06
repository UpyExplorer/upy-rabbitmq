#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import upy_rabbitmq

version = upy_rabbitmq.__version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="upy-rabbitmq",
    version=version,
    author="Fernando Celmer",
    author_email="email@fernandocelmer.com",
    description="Basic RabbitMQ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UpyExplorer/upy-rabbitmq",
    packages=[
        'upy_rabbitmq',
    ],
    include_package_data=True,
    install_requires=[
        'pika==1.3.2',
        'python-dotenv==1.0.0',
        'rich==13.5.2',
        'pydantic==2.1.1'
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    zip_safe=False
)
