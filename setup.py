from setuptools import setup, find_packages
from pathlib import Path

long_description = Path("README.md").read_text(encoding="utf-8") if Path("README.md").exists() else ""

setup(
    name="mlproject",
    version="0.0.1",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
)
