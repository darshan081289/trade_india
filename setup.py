from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="trade_india",
    version="0.0.1",
    description="Trade India Integration for ERPNext",
    author="Darshan Patel",
    author_email="darshan.patel@quarkssystems.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)