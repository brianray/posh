from distutils.core import setup
from distutils.extension import Extension

setup(name='posh',
      version="0.1",
      packages=['posh', ],
      package_dir={'posh': 'src/posh'},
      ext_modules=[Extension('posh.core',
                              sources=['src/posh_core/posh_python_extension.cpp',
                                       'src/posh_core/posh.cpp'],
                              headers=['src/posh_core/posh.h']
                              ), ])
