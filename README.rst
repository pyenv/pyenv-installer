pyenv installer
===============

This tool installs `pyenv <https://github.com/pyenv/pyenv>`__ and friends. It is inspired by `rbenv-installer <https://github.com/rbenv/rbenv-installer>`__.

Installation / Update / Uninstallation
--------------------------------------

Prerequisites
-------------
In general, compiling your own Python interpreter requires the installation of the
appropriate libraries and packages.  The `installation wiki
<https://github.com/pyenv/pyenv/wiki/Common-build-problems>`__ provides a list of these for common
operating systems.

Install:

.. code:: bash

    $ curl -L https://pyenv.run | bash
    
``pyenv.run`` redirects to the install script in this repository and the invocation above is equivalent to::

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

(Not released yet)
~~~~~~~~~~~~~~~~~~

-  Remove experimental PyPi support and replace with a dummy package.

20150113
~~~~~~~~

-  Initial release on PyPi.

20130601
~~~~~~~~

-  Initial public release.


License
-------

MIT - see [License file](LICENSE).
