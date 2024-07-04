# load .bashrc
. ~/.bashrc

# activate virtual python environment
pyenv activate venv_portfolio

# add server execute file path
export DJANGO_SETTINGS_MODULE=config.settings.local
