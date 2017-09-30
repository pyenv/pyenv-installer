import sys
from setuptools import setup
from setuptools.command.install import install

project_url = 'https://github.com/yyuu/pyenv-installer'
install_command = 'curl -L https://raw.githubusercontent.com/pyenv/' \
                  'pyenv-installer/master/bin/pyenv-installer | bash'

with open('pypi-readme.rst') as file:
    long_description = file.read()


class NoInstall(install):
    def run(self):
        sys.exit(
            "################ NOTE ################\n"
            "This package is not installable with pip. Install it with:\n\n"
            "%s\n\n"
            "See full instructions at %s\n" 
            "######################################\n" % (
                install_command, project_url))

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
