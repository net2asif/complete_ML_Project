from setuptools import setup, find_packages
import os
from typing import List


# HYPEN_E_DOT='-e .'
 
def get_requirements(filepath:str)->List[str]:

    #this function will return the list of requirements
    with open(filepath) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

        return requirements
 
setup(
    name='Machine learning project',
    version='0.0.1',
    description='This is end to end Machine Learning project',
    author='Asif',
    author_email='net2asif5050@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)