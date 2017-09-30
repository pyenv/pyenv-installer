import sys
from setuptools import setup
from setuptools.command.install import install

project_url = 'https://github.com/yyuu/pyenv-installer'

with open('pypi-readme.rst') as file:
    long_description = file.read()


class NoInstall(install):
    def run(self):
        sys.exit("NOTE: this package is not installable with pip."
                 "Please follow instructions on %s" % project_url)

setup(
    version='0.0.0',
    name='pyenv',
    author='Yamashita, Yuu',
    author_email='peek824545201@gmail.com',
    url=project_url,
    description='pyenv project placeholder package',
    long_description=long_description,
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
