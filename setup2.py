from distutils.core import setup, Extension
import py2exe
import sys
import re

# Use build_ext from Cython if found
command_classes = {}
try:
    import Cython.Distutils
    command_classes['build_ext'] = Cython.Distutils.build_ext
    has_cython = True
except:
    has_cython = False

ext = '.pyx' if has_cython else '.c'

from numpy import get_include as numpy_get_include
numpy_include_dir = [numpy_get_include()]

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('CRISPResso2/CRISPRessoShared.py').read(),
    re.M
    ).group(1)

ext_modules = [
        Extension("CRISPResso2.CRISPRessoCOREResources", ["CRISPResso2/CRISPRessoCOREResources" + ext], include_dirs=numpy_include_dir, extra_compile_args=['-w','-Ofast'] ),
        Extension("CRISPResso2.CRISPResso2Align", ["CRISPResso2/CRISPResso2Align" + ext], include_dirs=numpy_include_dir, extra_compile_args=['-w','-Ofast'] ),
                    ]
if has_cython:
    from Cython.Build import cythonize
    ext_modules = cythonize(ext_modules, language_level="2")

setup(
    name="CRISPResso2",
    #version=version,
    #author='Kendell Clement',
    #author_email='kclement@mgh.harvard.edu',
    #url='http://github.com/pinellolab/CRISPResso2',
    #package_dir={'CRISPResso2' : 'CRISPResso2'},
    #description="Software pipeline for the analysis of genome editing outcomes from deep sequencing data",
    console=[r'CRISPResso.py']
#    options = {
#        'includes': ['PyDes'],
#    }
    )