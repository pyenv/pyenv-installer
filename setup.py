"""Proof of concept for making pyenv pip installable."""
import distutils.core
from distutils.command.install import install
import subprocess


class PyenvInstall(install):
    def run(self):
        print(subprocess.check_output(['bash', 'bin/pyenv-installer']))


distutils.core.setup(
    name="pyenv",
    version='0.0.1',  # todo
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
    # data_files=[('bin', ['bm/b1.gif', 'bm/b2.gif'])]
)
