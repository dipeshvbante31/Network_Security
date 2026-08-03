from setuptools import find_packages,setup #it will scan through all folders and find __init__.py file and parent folder will become package it self
from typing import List

def get_requirements()->list[str]:

    """
    this function willl return list of requirements 

    """
    requirement_list:list[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read line from the file 

            lines =file.readlines()
            #process each line 

            for line in lines:
                requirement=line.strip()
                #igonre empty line and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="DipeshVB",
    author_email="dipeshbante611@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)