#!/usr/bin/env bash

checkout() {
  [ -d "$2" ] && (cd "$2"; git clone "$1")
}

if [ -z "$PYENV_PACKAGE_ARCHIVE" ]; then
  PYENV_PACKAGE_ARCHIVE="$(cd $(dirname "$0") && pwd)/pyenv-package.tar.gz"
fi

TMP_DIR=$(mktemp -d)

# Check ssh authentication if USE_SSH is present
if [ -n "${USE_SSH}" ]; then
  if ! command -v ssh 1>/dev/null 2>&1; then
    echo "pyenv: configuration USE_SSH found but ssh is not installed, can't continue." >&2
    exit 1
  fi

  # `ssh -T git@github.com' returns 1 on success
  # See https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection
  ssh -T git@github.com 1>/dev/null 2>&1 || EXIT_CODE=$?
  if [[ ${EXIT_CODE} != 1 ]]; then
      echo "pyenv: github ssh authentication failed."
      echo
      echo "In order to use the ssh connection option, you need to have an ssh key set up."
      echo "Please generate an ssh key by using ssh-keygen, or follow the instructions at the following URL for more information:"
      echo
      echo "> https://docs.github.com/en/repositories/creating-and-managing-repositories/troubleshooting-cloning-errors#check-your-ssh-access"
      echo
      echo "Once you have an ssh key set up, try running the command again."
    exit 1
  fi
fi

if [ -n "${USE_SSH}" ]; then
  GITHUB="git@github.com:"
else
  GITHUB="https://github.com/"
fi

# checkout to temporary directory.
checkout "${GITHUB}pyenv/pyenv.git"            "$TMP_DIR"
checkout "${GITHUB}pyenv/pyenv-doctor.git"     "$TMP_DIR"
checkout "${GITHUB}pyenv/pyenv-update.git"     "$TMP_DIR"
checkout "${GITHUB}pyenv/pyenv-virtualenv.git" "$TMP_DIR"

# create archive.
tar -zcf "$PYENV_PACKAGE_ARCHIVE" -C "$TMP_DIR" .

rm -rf $TMP_DIR
