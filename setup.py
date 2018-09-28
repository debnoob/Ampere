import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="battery",
    version="0.1.1-alpha",
    author="battery.py developers",
    author_email="nealde@uw.edu",
    description="A Python package for working with impedance data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://impedancepy.readthedocs.io/en/latest/",
    packages=setuptools.find_packages(),
    install_requires=['matplotlib>=2.0', 'numpy>=1.14', 'scipy>=1.0'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
