from setuptools import setup, find_packages

setup(
    name="matrixchain-hacker",
    version="1.0.0",
    author="Chauhan Pruthviraj",
    description="Hacker-style Matrix Chain Multiplication visualizer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "matrixchain=matrixchain.core:main"
        ]
    },
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="matrix multiplication dynamic programming algorithm visualization education",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/matrixchain/issues",
        "Source": "https://github.com/yourusername/matrixchain",
    },
)
