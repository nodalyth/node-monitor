from setuptools import setup, find_packages

setup(
    name="my-python-web3-project",
    version="0.1.0",
    description="A Python project using web3.py",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "web3",
        "PyYAML"
    ],
    python_requires=">=3.7",
)
