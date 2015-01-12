import distutils.core
from distutils.command.install import install
import subprocess


class PyenvInstall(install):
    def run(self):
        print(subprocess.check_output(['bash', 'bin/pyenv-installer']))


distutils.core.setup(
    name='pyenv',
    version='20150113',
    description='Installs pyenv and friends',
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
