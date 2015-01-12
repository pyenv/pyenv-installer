pyenv installer
===============

This tools is used to install ``pyenv`` and friends.

This plugin was inspired from
`rbenv-installer <https://github.com/fesplugas/rbenv-installer>`__.

Installation
------------

Install `pyenv <https://github.com/yyuu/pyenv>`__ and friends by
running:

::

    $ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

Updating
--------

To update pyenv and friends by running:

::

    $ pyenv update

Uninstallation
--------------

Everything of ``pyenv`` are installed within ``$PYENV_ROOT`` (default:
``~/.pyenv``). To uninstall, just removing it.

::

    $ rm -fr ~/.pyenv

Development and testing
-----------------------

This project contains a setup for vagrant to test the installer inside a
vagrant managed virtual image.

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

::

    $ cd /vagrant
    $ python setup.py install
    $ echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
    $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    $ source ~/.bashrc

Pyenv should be installed and responding now.


Version History
---------------

20130601
^^^^^^^^

-  Initial public release.

License
~~~~~~~

(The MIT License)

-  Copyright (c) 2013 Yamashita, Yuu

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
