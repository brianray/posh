from distutils.core import setup
from distutils.extension import Extension

setup(name='posh',
      version="0.1",
      packages=['posh'],
      package_dir={'posh': 'src/posh'},
      ext_modules=[Extension('posh.core',
                   sources=['src/posh_core/posh_python_extension.c'])])
