from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules = cythonize(Extension(
           "rect",                # our Cython source
           sources=["rect.pyx","Rectangle.cpp"],  # additional source file(s)
           language="c++",             # generate C++ code
      )))