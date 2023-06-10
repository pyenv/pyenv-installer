#!/usr/bin/env bash

set -e
[ -n "$PYENV_DEBUG" ] && set -x

if [ -z "$PYENV_ROOT" ]; then
  if [ -z "$HOME" ]; then
    printf "$0: %s\n" \
      "Either \$PYENV_ROOT or \$HOME must be set to determine the install location." \
      >&2
    exit 1
  fi
  export PYENV_ROOT="${HOME}/.pyenv"
fi

colorize() {
  if [ -t 1 ]; then printf "\e[%sm%s\e[m" "$1" "$2"
  else echo -n "$2"
  fi
}

# Checks for `.pyenv` file, and suggests to remove it for installing
if [ -d "${PYENV_ROOT}" ]; then
  { echo
    colorize 1 "WARNING"
    echo ": Can not proceed with installation. Kindly remove the '${PYENV_ROOT}' directory first."
    echo
  } >&2
    exit 1
fi

failed_checkout() {
  echo "Failed to git clone $1"
  exit -1
}

checkout() {
  [ -d "$2" ] || git -c advice.detachedHead=0 clone --branch "$3" --depth 1 "$1" "$2" || failed_checkout "$1"
}

if ! command -v git 1>/dev/null 2>&1; then
  echo "pyenv: Git is not installed, can't continue." >&2
  exit 1
fi

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

checkout "${GITHUB}pyenv/pyenv.git"            "${PYENV_ROOT}"                           "${PYENV_GIT_TAG:-master}"
checkout "${GITHUB}pyenv/pyenv-doctor.git"     "${PYENV_ROOT}/plugins/pyenv-doctor"      "master"
checkout "${GITHUB}pyenv/pyenv-update.git"     "${PYENV_ROOT}/plugins/pyenv-update"      "master"
checkout "${GITHUB}pyenv/pyenv-virtualenv.git" "${PYENV_ROOT}/plugins/pyenv-virtualenv"  "master"

if ! command -v pyenv 1>/dev/null; then
  { echo
    colorize 1 "WARNING"
    echo ": seems you still have not added 'pyenv' to the load path."
    echo
  } >&2

  { # Without args, `init` commands print installation help
    "${PYENV_ROOT}/bin/pyenv" init || true
    "${PYENV_ROOT}/bin/pyenv" virtualenv-init || true
  } >&2
fi
