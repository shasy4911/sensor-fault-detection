from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """This function will return a list of requirements."""
    requirement_list:List[str] = []
    return requirement_list

    """Write a code to read requirements.txt file and append each requirement in each requirement variable"""

setup(

    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="shashanksaurav4911@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)

