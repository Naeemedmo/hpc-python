from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
     ext_modules=cythonize([Extension("mandel_cyt",["mandel_cyt.pyx"], include_dirs=[numpy.get_include()])])
)
