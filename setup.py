from setuptools import find_packages,setup
from typing import List # typing supports for hintting


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[] # work fine without varible
    """Initialization:

The line requirements = [] initializes the requirements variable as an empty list. This ensures that requirements is defined and is of type List before any lines from the file are read.
Fallback/Default Value:
In case there are issues reading the file (like if the file is empty), requirements will at least be an empty list, preventing potential errors later in the code that assumes requirements is always a list.
Code Clarity:
Initializing the variable at the beginning of the function makes the code clearer 
and more readable. It immediately indicates to the reader that requirements is intended
 to be a list that will hold the requirements read from the file.
    """
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #read the all lines in files into the list
        requirements=[req.replace("\n","") for req in requirements] # remove the mewline charactere
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Krish',
author_email='krishnaik06@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)

setup(
name='mlproject',
version='0.0.1',
author='vijay vardhan',
author_email='pvijayavardhan@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)