from setuptools import find_packages,setup
from typing import List
import os

def get_requirements():
        """
        This function will return list of requirements
        """
        requirement_lst:list[str]=[]
        try:
                with open('requirements.txt',"r") as file:
                    lines=file.readlines()

                    for line in lines:
                           requirement=line.strip()

                           ## ignore the empty lines and -e.

                           if requirement and requirement!='-e.':
                                  requirement_lst.append(requirement)
        except FileNotFoundError:
               print("requirements.txt not found")

        return requirement_lst


setup(
       name="NetworkSecurity",
       version="0.0.1",
       author="Yuyutsu",
       author_email="bpin333@gmail.com",
       packages=find_packages(),
       install_requires=get_requirements()
)