# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open('README.md', 'r') as f:
  readme =  f.read()

requirements = [
    "transformers>=4.6",
    "sentencepiece",
    "emoji",
    "pythainlp>=2.2.4",
    # "sefr_cut",
    "tokenizers",
]


setup(
    name="thaixtransformers",
    version="0.1.0",
    description="ThaiXtransformers: Use Pretraining RoBERTa based Thai language models from VISTEC-depa AI Research Institute of Thailand.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="PyThaiNLP",
    author_email="",
    url="https://github.com/pythainlp/thaixtransformers",
    packages=find_packages(exclude=["notebooks", "notebooks.*", "external_scripts", "external_scripts.*"]),
    python_requires=">=3.8",
    package_data={},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
        "thainlp",
        "NLP",
        "natural language processing",
        "text analytics",
        "text processing",
        "localization",
        "computational linguistics",
        "ThaiNLP",
        "Thai NLP",
        "Thai language",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    project_urls={
        "Documentation": "https://github.com/pythainlp/thaixtransformers",
        "Source Code": "https://github.com/pythainlp/thaixtransformers",
        "Bug Tracker": "https://github.com/pythainlp/thaixtransformers/issues",
    },
)
