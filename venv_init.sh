#!/bin/bash
if not [ -f "$HOME/.pyenv/bin/pyenv" ]; then
  curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
  echo "export PATH=\"${PYENV_ROOT}/bin:\$PATH\"" >> ~/.zshrc
  echo "eval \"\$(pyenv init -)\"" >> ~/.zshrc
  echo "eval \"\$(pyenv virtualenv-init -)\"" >> ~/.zshrc
fi

if not [ -d "$HOME/.pyenv/versions/3.8.17" ]; then
  pyenv install 3.8.17
fi

pyenv local 3.8.17
virtualenv -p $HOME/.pyenv/versions/3.8.17/bin/python3 venv
source ./venv/bin/activate

if [ -f ".gitignore" ]; then
  if [ `grep venv .gitignore|wc -l` -gt 0 ]; then
    echo "venv" >> .gitignore
  fi
fi
