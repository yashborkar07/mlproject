from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.01",
    author="yash",
    author_email="yashborkar07@gmail.com",
    packages=find_packages(),  #finds all the __init__ packages 
    install_requires=get_requirements("requirements.txt") #we cant keep editting this so we given packages in requirement and extract it here
)