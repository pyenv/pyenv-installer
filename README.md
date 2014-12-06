# Proof of conecpt: setup.py enhanced pyenv installer

This is a little lab to show that pyenv can be made installable with standard
Python packaging tools (a.k.a. pip).

It turns out, that plugging the installer into pip is borderline trivial. The actual challenges are getting that tested in all kinds of environemnts and automating the shell integration and installing the actual dependencies for compiling Python.

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

## The real problems

* automate shell integration (a.k.a adding stuff to the correct user profile without pissing them off)

* automate dependency installations (a.k.a automate solutions for [common build problems](https://github.com/yyuu/pyenv/wiki/Common-build-problems))

## Todo test it on TestPyPI

* register it on [testPyPi](https://wiki.python.org/moin/TestPyPI) test and try from there
