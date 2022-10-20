from setuptools import setup

setup(
    name="gh-page-test",
    version="0.0.0",
    python_requires=">=3.9.7",
    extras_require={
        "dev": [
            "sphinx",
            # "sphinx-markdown-tables",
            # "sphinx-rtd-theme",
            # "sphinxcontrib-mermaid",
            # "sphinxcontrib-plantuml",
        ]
    },
)
