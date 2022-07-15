# Standard library imports

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terminalcolorpy",
    version="2.0.0",
    author="novusys",
    author_email="amarftw1@gmail.com",
    description="Simple package to print colored messages using ASCI to the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/novusys/terminalcolorpy/",
    project_urls={
        "Bug Tracker": "https://github.com/novusys/terminalcolorpy/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=["terminalcolorpy"],
    install_requires=[],
    python_requires=">=3.10",
    license="MIT",
)
