from setuptools import find_packages,setup
from typing import List

cst = "-e."
def get_requirements(file_path:str)->list[str]:
    """
    this function will return a list of requirements """
    requirement=[]
    with open("requirement.txt") as file_obj:
        requirement = file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]
        
        if cst in requirement:
            requirement.remove(cst)
    return requirement
setup(
    name="mlproject",
    version="0.0.1",
    author="otman",
    author_email="otmanaitmoulay@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt")
    
)