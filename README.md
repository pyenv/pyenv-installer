# Proof of conecpt: setup.py enhanced pyenv installer

This is a little lab to show that pyenv can be made installable with standard
Python packaging tools (a.k.a. pip).

It turns out, that plugging the installer into pip is borderline trivial. The actual challenges are getting that tested in all kinds of environemnts and automating the shell integration and installing the actual dependencies for compiling Python (but this is not automated by the existing installer yet either, so this should be done there (if at all)).

## Testing locally

If you don't know vagrant yet: just [install the latest package](https://www.vagrantup.com/downloads.html), open a shell in this project directory and say 

    $ vagrant up
    $ vagrant ssh

Now you are inside the vagrant container and your prompt should like something like `vagrant@vagrant-ubuntu-trusty-64:~$`

The project (this repository) is mapped into the vagrant image at /vagrant

    $ cd /vagrant
    $ python setup.py install
    $ echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
    $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    $ source ~/.bashrc
    
Done. pyenv is installed and responding.

## It's on TestPyPI

`pip install --egg -i https://testpypi.python.org/pypi pyenv`

Anybody know how to get rid of the `--egg` param?

## The real problems (inherited from the original installer)

* shell integration not automated

* dependency installation for building python version not automated - see [common build problems](https://github.com/yyuu/pyenv/wiki/Common-build-problems))
