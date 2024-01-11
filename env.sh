sudo apt install python3-pip
sudo pip3 install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple
sudo pip3 install pipenv -i https://pypi.tuna.tsinghua.edu.cn/simple
pipenv --python 3
pipenv run pip install -r requirements.txt
env_path=$(pipenv --venv)
cp -r mkdocs_toc_plugin ${env_path}
