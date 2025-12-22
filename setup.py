from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of valid package requirements from a requirements.txt file.
    Ignores editable installs (-e .), comments (#...), and empty lines.
    """
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj.readlines()]

        requirements = [
            req for req in requirements if req and not req.startswith("-e") and not req.startswith("#")
        ]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Sourav',
    author_email='moripallisourav@gmail.com',
    packages=find_packages(),              
    install_requires=get_requirements('requirements.txt'),
)
