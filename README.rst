pyenv installer
===============

This tool installs `pyenv <https://github.com/pyenv/pyenv>`__ and friends. It is inspired by `rbenv-installer <https://github.com/fesplugas/rbenv-installer>`__.

Installation / Update / Uninstallation
--------------------------------------

There are two ways to install pyenv.
The PyPi support is not tested by many users yet, so the
direct way is still recommended if you want to play it safe.

Github way (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~

Install:

.. code:: bash

    $ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

Update:

.. code:: bash

    $ pyenv update

Uninstall: ``pyenv`` is installed within ``$PYENV_ROOT``
(default: ``~/.pyenv``). To uninstall, just remove it:

.. code:: bash

    $ rm -fr ~/.pyenv
    
and remove these three lines from ``.bashrc``:

.. code:: bash

    export PATH="~/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

If you need, export USE_GIT_URI to use git:// instead of https:// for git clone.

PyPi way
~~~~~~~~

**WARNING** still a very hacky proof of concept. Does not work with Python 3 at all yet and in Python 2 only with 
the use of the --egg parameter.

Install::

    $ pip install --egg pyenv


In the current implementation updates and uninstallation works exactly like
the github way.

**NOTE**: ``pip freeze`` will not show pyenv as installed as this tool is just a
thin wrapper around the shell install script.

Development and testing
-----------------------

The `project on github <https://github.com/pyenv/pyenv-installer>`__ contains
a setup for vagrant to test the installer inside a vagrant managed virtual image.

If you don't know vagrant yet: just `install the latest
package <https://www.vagrantup.com/downloads.html>`__, open a shell in
this project directory and say

::

    $ vagrant up
    $ vagrant ssh

Now you are inside the vagrant container and your prompt should like
something like ``vagrant@vagrant-ubuntu-trusty-64:~$``

The project (this repository) is mapped into the vagrant image at
/vagrant

.. code:: bash

    $ cd /vagrant
    $ python setup.py install
    $ echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
    $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    $ source ~/.bashrc

Pyenv should be installed and responding now.


Version History
---------------

20150113
~~~~~~~~

-  Initial release on PyPi.

20130601
~~~~~~~~

-  Initial public release.


License
-------

(The MIT License)

-  Copyright (c) 2013-2015 Yamashita, Yuu
-                2015 Oliver Bestwalter (PyPi support)

| Permission is hereby granted, free of charge, to any person obtaining
| a copy of this software and associated documentation files (the
| "Software"), to deal in the Software without restriction, including
| without limitation the rights to use, copy, modify, merge, publish,
| distribute, sublicense, and/or sell copies of the Software, and to
| permit persons to whom the Software is furnished to do so, subject to
| the following conditions:

| The above copyright notice and this permission notice shall be
| included in all copies or substantial portions of the Software.

| THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
| EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
| MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
| NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
| LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
| OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
| WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
