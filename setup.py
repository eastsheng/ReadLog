"""run this
python setup.py sdist
pip install .
"""

# from distutils.core import setup
from setuptools import setup, find_packages

setup(
name         = 'ReadLog',
version      = '1.1.0',
py_modules   = ['ReadLog'],
author       = 'CHENDONGSHENG',
author_email = 'eastsheng@hotmail.com',
packages=find_packages('src'),
package_dir={'': 'src'},
install_requires=open('requirements.txt').readlines(),
url          = 'https://github.com/eastsheng',
description  = 'Read themo info from lammps output file or log file'
)

