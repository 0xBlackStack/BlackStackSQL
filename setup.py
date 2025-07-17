from setuptools import setup, find_packages

setup(
    name="blackstacksql",
    version="1.0.0",
    author="Reflex Coder / BlackStack Unit",
    description="Advanced Modular SQL Injection Toolkit",
    long_description=open("BlackStackSQL/README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/0xBlackStack/BlackStackSQL",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "requests",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "blackstacksql=main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
