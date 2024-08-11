from setuptools import find_packages,setup
from typing import List


HYPHAN_E_DOT="-e ."
def get_requirement(find_path:str)->List[str]:
    """
    Get all the packages stired in requirements.txt.
    """
    requirements=[]
    with open(find_path) as f:
        requirements = f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHAN_E_DOT in requirements:
            requirements.remove(HYPHAN_E_DOT)

    return requirements

setup(
    name='abuPackage',
    version='0.0.1',
    author='Abuzar',
    author_email='abuzarkhan.ip123@gmail.com',
    packages=find_packages(),
    install_requires=[get_requirement("requirements.txt")],
)