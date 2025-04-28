from setuptools import setup, find_packages

setup(
    name="scraper-agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "playwright>=1.40.0",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
    ],
) 