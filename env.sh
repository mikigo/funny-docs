sudo apt install python3-pip
sudo pip3 install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple
sudo pip3 install pipenv -i https://pypi.tuna.tsinghua.edu.cn/simple
pipenv --python 3
pipenv run pip install -r requirements.txt
cd mkdocs-toc-plugin-0.0.1
pipenv run python setup.py install
cd -