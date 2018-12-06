import distutils.core
from distutils.command.install import install
import subprocess


class PyenvInstall(install):
    def run(self):
        print(subprocess.check_output(['bash', 'bin/pyenv-installer']))

with open('README.rst') as file:
    long_description = file.read()

distutils.core.setup(
    version='20150113',
    name='pyenv',
    author='Yamashita, Yuu',
    url='https://github.com/pyenv/pyenv-installer',
    description='Tool to install pyenv and friends',
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
    cmdclass=dict(install=PyenvInstall),
)
