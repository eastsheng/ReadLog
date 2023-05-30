"""run this
python setup.py sdist
pip install .
"""

from distutils.core import setup

setup(
name         = 'ReadLog',
version      = '1.1.0',
py_modules   = ['ReadLog'],
author       = 'CHENDONGSHENG',
author_email = 'eastsheng@hotmail.com',
url          = 'https://github.com/eastsheng',
description  = 'Read themo info from lammps output file or log file'
)

