"""Proof of concept for making pyenv pip installable.

Can be used as a 'real' script.

Install locally and editable: `pip install --editable .`

Uninstall: `pip uninstall update-bridge-tool`

"""
import distutils.core
from distutils.command.install import install
import os
import subprocess


class my_install(install):
    def run(self):
        #install.run(self)  # no python no run?
        print(os.getcwd())
        print(subprocess.check_output(['bash', 'bin/pyenv-installer']))

distutils.core.setup(
    name="pyenv",
    version='0.0.0.1',
    cmdclass=dict(install=my_install)
)
