from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    #reading lines in requirements file
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        #removing -e . from requirements file
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name= 'ci_cd_mlproject',
    version='0.0.1',
    author='Arun',
    author_email='arun02negime@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)