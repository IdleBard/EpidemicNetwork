rm -rf .\venv\

py -m pip install --user --upgrade pip
py -m pip --version
py -m pip install --user virtualenv

py -m venv venv

source ./venv/Scripts/Activate

pip install igraph
# pip install networkx
pip install pycairo