from setuptools import find_namespace_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    get_requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='RegressorProject',
    version='0.0.1',
    author='sksuraj',
    author_email='sksuraj6077@gmail.com',
    install_reuires=get_requirements('requirements.txt'),
    packages=find_namespace_packages()
    )