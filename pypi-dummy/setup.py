import sys

from setuptools import setup
from setuptools.command.install import install

LONG_DESCRIPTION = """\
pyenv
=====

pyenv lets you easily switch between multiple versions of Python. It's simple, 
unobtrusive, and follows the UNIX tradition of single-purpose tools that do one 
thing well.

**NOTE:** This is a placeholder package. 
pyenv is a collection of shell scripts and not installable with pip.

See `installation instructions <https://github.com/pyenv/pyenv#installation>` 
for more information.
"""

ERROR_MSG = """\
############################ NOTE ############################
We are sorry, but this package is not installable with pip.

Please read the installation instructions at:
 
https://github.com/pyenv/pyenv#installation
##############################################################
"""


class NoInstall(install):
    def run(self):
        sys.exit(ERROR_MSG)


setup(
    version='0.0.0',
    name='pyenv',
    author='Yamashita, Yuu',
    author_email='peek824545201@gmail.com',
    url="https://github.com/pyenv/pyenv",
    description='pyenv project placeholder package',
    long_description=LONG_DESCRIPTION,
    license='MIT',
    platforms=['UNIX'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Unix Shell',
        'Topic :: Software Development :: Interpreters',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    cmdclass={'install': NoInstall},
)
