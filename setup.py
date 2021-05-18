from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="VNA",
    version="0.1.0",
    description="VNA control",
    long_description=readme,
    author=["Ashutosh Bhudia"],
    author_email=[
        "ashu.bhudia@ece.ubc.ca",
    ],
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
