from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hellocash",
    version="0.2.0",
    description="Unofficial Python SDK for HelloCash API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Paul Harrer",
    author_email="mail@paulharrer.at",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    project_urls={
        "GitHub": "https://github.com/PaulHarrer/hellocash-python",
    },
)
