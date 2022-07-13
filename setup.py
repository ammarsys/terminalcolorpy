# Standard library imports

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terminalcolorpy",
    version="0.1.2",
    author="ammarsys",
    author_email="amarftw1@gmail.com",
    description="Simple package to print colored messages using ASCI to the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ammarsys/terminalcolorpy/",
    project_urls={
        "Bug Tracker": "https://github.com/ammarsys/terminalcolorpy/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    packages=["pyaww"],
    install_requires=[],
    python_requires=">=3.6",
    license="MIT",
)
