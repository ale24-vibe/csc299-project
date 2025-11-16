from setuptools import setup, find_packages

setup(
    name="tasks5",
    version="0.1.0",
    description="Small teaching-focused tasks manager",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
