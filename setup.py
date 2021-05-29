import setuptools


with open("requirements.txt", "r") as fp:
    required = fp.read().splitlines()

setuptools.setup(
    name="paperwhisperer",
    version="0.1.0",
    author="Valerio Velardo",
    author_email="valerio@thesoundofai.com",
    description="Speech summaries of arxiv papers retrieved via keyword "
                "search",
    url="https://github.com/musikalkemist/paperwhisperer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.7",
    install_requires=required,
    entry_points={
        "console_scripts": [
            "create_summaries = paperwhisperer.create_summaries:create_summaries"
        ]
    },
    extras_require={
        "test": ["pytest"]
    }
)
