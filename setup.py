from __future__ import print_function  # noqa
from future.utils import raise_from  # noqa
from distutils.core import setup
from distutils import spawn
from setuptools.command.test import test as _test
from setuptools.command.test import test as TestCommand
from setuptools import Command
from setuptools import Extension
import subprocess
import os
import platform


CODE_DIRECTORY = 'posh'
DOCS_DIRECTORY = 'docs'
TESTS_DIRECTORY = 'tests'
PYTEST_FLAGS = ['--doctest-modules']
EXTRA_COMPILER_ARGS = ["-std=c++11", ]


def check_call(args):
    try:
        subprocess.check_call(args)
        return True
    except Exception as e:
        print(str(e))
    return False


if platform.system() == 'Darwin':
    if check_call(['clang++', '--version']):
        os.environ["CXX"] = "clang++"
    EXTRA_COMPILER_ARGS += ["-stdlib=libc++",
                            "-mmacosx-version-min=10.7"]
elif platform.system() == "Linux":
    # CXXFLAGS=-c -g -Wall -std=c++11 {{INC}}
    pass


class test(_test):

    def finalize_options(self):
        _test.finalize_options(self)
        self.test_args.insert(0, 'discover')


def get_project_files():
    """Retrieve a list of project files, ignoring hidden files.
    :return: sorted list of project files
    :rtype: :class:`list`
    """
    if is_git_project() and has_git():
        return get_git_project_files()

    project_files = []
    for top, subdirs, files in os.walk('.'):
        for subdir in subdirs:
            if subdir.startswith('.'):
                subdirs.remove(subdir)

        for f in files:
            if f.startswith('.'):
                continue
            project_files.append(os.path.join(top, f))

    return project_files


def is_git_project():
    return os.path.isdir('.git')


def has_git():
    return bool(spawn.find_executable("git"))


def git_ls_files(*cmd_args):
    """Run ``git ls-files`` in the top-level project directory. Arguments go
    directly to execution call.
    :return: set of file names
    :rtype: :class:`set`
    """
    cmd = ['git', 'ls-files']
    cmd.extend(cmd_args)
    return set(subprocess.check_output(cmd).splitlines())


def get_git_project_files():
    """Retrieve a list of all non-ignored files, including untracked files,
    excluding deleted files.
    :return: sorted list of git project files
    :rtype: :class:`list`
    """
    cached_and_untracked_files = git_ls_files(
        '--cached',  # All files cached in the index
        '--others',  # Untracked files
        # Exclude untracked files that would be excluded by .gitignore, etc.
        '--exclude-standard')
    uncommitted_deleted_files = git_ls_files('--deleted')

    # Since sorting of files in a set is arbitrary, return a sorted list to
    # provide a well-defined order to tools like flake8, etc.
    return sorted(cached_and_untracked_files - uncommitted_deleted_files)


def _lint():
    """Run lint and return an exit code."""
    # Flake8 doesn't have an easy way to run checks using a Python function, so
    # just fork off another process to do it.

    # Python 3 compat:
    # - The result of subprocess call outputs are byte strings, meaning we need
    #   to pass a byte string to endswith.
    project_python_files = [filename for filename in get_project_files()
                            if filename.endswith(b'.py')]
    try:
        retcode = subprocess.call(
            ['flake8', '--max-complexity=10'] + project_python_files)
    except Exception as e:
        print(e)
        print("is flake8 installed")
        retcode = -1
    if retcode == 0:
        print_success_message('No style errors')
    return retcode


def print_success_message(message):
    """Print a message indicating success in green color to STDOUT.
    :param message: the message to print
    :type message: :class:`str`
    """
    try:
        import colorama
        print(colorama.Fore.GREEN + message + colorama.Fore.RESET)
    except ImportError:
        print(message)


def _test():
    """Run the unit tests.
    :return: exit code
    """
    # Make sure to import pytest in this function. For the reason, see here:
    # <http://pytest.org/latest/goodpractises.html#integration-with-setuptools-test-commands>  # NOPEP8
    import pytest
    # This runs the unit tests.
    # It also runs doctest, but only on the modules in TESTS_DIRECTORY.
    return pytest.main(PYTEST_FLAGS + [TESTS_DIRECTORY])


def _test_all():
    """Run lint and tests.
    :return: exit code
    """
    return _lint() + _test()


# The following code is to allow tests to be run with `python setup.py test'.
# The main reason to make this possible is to allow tests to be run as part of
# Setuptools' automatic run of 2to3 on the source code. The recommended way to
# run tests is still `paver test_all'.
# See <http://pythonhosted.org/setuptools/python3.html>
# Code based on <http://pytest.org/latest/goodpractises.html#integration-with-setuptools-test-commands>  # NOPEP8
class TestAllCommand(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        # These are fake, and just set to appease distutils and setuptools.
        self.test_suite = True
        self.test_args = []

    def run_tests(self):
        raise SystemExit(_test_all())


citar_sources = """./external/citar/src/corpus/BrownCorpusReader.cpp
./external/citar/src/corpus/BrownCorpusReaderPrivate.cpp
./external/citar/src/cwrap/cwrap.cpp
./external/citar/src/tagger/hmm/HMMTagger.cpp
./external/citar/src/tagger/hmm/HMMTaggerPrivate.cpp
./external/citar/src/tagger/hmm/LinearInterpolationSmoothing.cpp
./external/citar/src/tagger/hmm/LinearInterpolationSmoothingPrivate.cpp
./external/citar/src/tagger/hmm/Model.cpp
./external/citar/src/tagger/hmm/ModelPrivate.cpp
./external/citar/src/tagger/wordhandler/KnownWordHandler.cpp
./external/citar/src/tagger/wordhandler/SuffixWordHandler.cpp
./external/citar/src/tagger/wordhandler/WordSuffixTree.cpp""".split("\n")

posh_sources = """src/posh_core/posh_python_extension.cpp
src/posh_core/rule.cpp
src/posh_core/posh.cpp
src/posh_core/train.cpp""".split("\n")

include_dirs = """./external/citar/include
./src/posh_core/""".split("\n")


def touch(fname):
    if os.path.exists(fname):
        os.utime(fname, None)
    else:
        open(fname, 'a').close()


class MakeFileCommand(Command):
    """setuptools Command"""
    description = "run my command"
    user_options = []  # tuple()

    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        """make the makefile"""
        try:
            from bottle import template
        except Exception:
            print("please install bottle (pip install bottle) to run makefile")
            return
        global include_dirs
        filenames = [('posh_cli', './utils/posh_cli.cpp'), ]
        include_dirs.append('utils')
        exclude_list = ('posh_python_extension', )
        for sourcs in citar_sources + posh_sources:
            base_name = os.path.splitext(os.path.basename(sourcs))[0]
            if base_name not in exclude_list:
                filenames.append((base_name, sourcs))
            base = os.path.dirname(sourcs)
            if base not in include_dirs:
                include_dirs.append(base)
        template_str = '''
# Do not edit this file directly, generate with:
#     $ python setup.py makefile
# rewquires bottle (pip install bottle)

CXX={{CXX}}
CXXFLAGS=-c -g -Wall -std=c++11 {{INC}}

all: posh_cli

posh_cli: \\
% for filename, full in filenames:
{{filename}}.o \\
% end

\t$(CXX) \\
% for filename, full in filenames:
{{filename}}.o \\
% end
 -o posh_cli

# -----------------
% for filename, full in filenames:

{{filename}}.o: {{full}}
\t$(CXX) $(CXXFLAGS) {{full}}
% end

clean:
\trm posh_cli  || true
\trm *.o  || true
\trm ./external/citar/include/citar/config.hh  || true

'''
        INC = " ".join(["-I{}".format(x) for x in include_dirs])
        out = template(template_str,
                       **dict(CXX=os.environ.get("CXX", "g++"),
                              INC=INC,
                              filenames=filenames))

        f = open("Makefile", "w")
        f.write(out)
        f.close()
        print("wrote Makefile\n")
    touch("./external/citar/include/citar/config.hh")


posh_ext = Extension('posh.core',
                     include_dirs=include_dirs,
                     extra_compile_args=EXTRA_COMPILER_ARGS,
                     sources=posh_sources + citar_sources)

setup(name='posh',
      version="0.1",
      packages=['posh', ],
      package_dir={'posh': 'src/posh'},
      ext_modules=[posh_ext, ],
      install_requires=[
          "nltk==3.0.4",
      ],
      cmdclass={'test': TestAllCommand,
                'makefile': MakeFileCommand},
      tests_require=[
          'setuptools==18.1',
          'pytest==2.5.1',
          'mock==1.3.0',
          'flake8==2.1.0'])
