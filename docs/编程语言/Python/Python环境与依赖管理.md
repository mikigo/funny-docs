---
counter: True
---

# Python环境与依赖管理

```shell
# ==================================
# Author : mikigo
# ==================================
```


Python有一大特点，即具有强大的标准库和第三方库。在开发过程中可能会用到第三方库，那么就需要对其进行安装和管理。基于一定的工具链，Python也能写出优雅标准的项目代码，将依赖管理玩的明明白白。

## pip

pip 是 Python 标准库的一个包，从 Python3.4 开始 pip 已经内置在 Python 中。Python 有成千上万的宝藏库，它们被放置在一个统一的仓库 `pypi`。pip 在这个仓库中充当着管理员的角色，可以将需要的库从 Pypi 取出来，安装并管理这些库。

由于大多数的第三方库都发布在 pypi，所以通过pip就可以安装95%以上的第三方库，体量在包安装这方面是大哥级别。pip还有一大优势就是在安装库的同时会把库所需要的依赖也一并进行安装。综上所述，在单一的项目环境中推荐使用它，简单便捷。

如果有两个及以上的项目环境就不建议去使用pip，会出现环境冲突且难以管理。如果一定要使用那么就需要搭配上环境管理工具。

### 安装

如果 Python 环境没有 pip 工具可以通过以下两种方法进行安装。

```shell
sudo apt-get install python-pip
```
还有种方法：

在 https://pypi.org/project/pip/#files 中下载pip安装文件，然后解压到 `python scripts` 目录中，执行 `python setup.py install` 命令安装即可；

许多人抱怨 pip 命令安装 Python 库很慢或者是安装过程中失败，其实是 pip 源的问题，将其更换为我们国内源即可；

1.临时设定：

```plain
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package matplotlib
```
2.设置为默认：

```plain
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
设为默认后，以后安装库都是从清华源下载，而且无需再加镜像源网址。
### 快速配置环境

通过 pip list 命令可以预览当前环境下的依赖包：

```plain
:~$ pip list
Package       Version 
------------- --------
asn1crypto    0.24.0  
colorama      0.3.7   
configparser  3.5.0b2 
cryptography  2.6.1   
decorator     4.3.0
```
通过 pip install package_name 命令安装 Python 包：
以 requests 包举例说明：

```plain
~$ pip install requests
Collecting requests
......
Successfully installed certifi-2021.10.8 chardet-4.0.0 idna-2.10 requests-2.27.1 urllib3-1.26.16
```
还可以通过pip install requests==<版本号>来指定包的版本号进行安装：
```plain
pip install requests==2.27.1
```
如果我们想将安装好的这些包及依赖信息全部记录下来，就可以通过pip freeze命令将信息记  在requirements.txt中。
```plain
pip freeze > requirements.txt
```
当我们需要在一个新的python环境中引入当前的依赖时使用以下命令即可。
```plain
pip  install -r requirements.txt
```
还可以通过 pipreqs 进行导包操作：
```plain
~$ pip install pipreqs
~$ pipreqs ./  此命令也是生成一个requirements.txt文件在当前项目目录下
```
如果环境中存在 requirements.txt 文件，需要使用以下命令导出 requirements.txt 文件：
```plain
pipreqs ./ --encoding=utf-8 --force
```
注意可能在使用时会发现：
```plain
~$ pipreqs ./
Traceback (most recent call last):
  File "/home/uos/.local/bin/pipreqs", line 6, in <module>
    from pipreqs.pipreqs import main
  File "/home/uos/.local/lib/python2.7/site-packages/pipreqs/pipreqs.py", line 51, in <module>
    from pipreqs import __version__
ImportError: cannot import name __version__
```
报错了怎么办？

不要慌张，其实这是因为此环境下版本不可用，换个版本就好啦！

```plain
~$ pip install pipreqs==100
Collecting pipreqs==100
Could not find a version that satisfies the requirement pipreqs==100 (from versions: 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7, 0.1.8, 0.1.9, 0.2.0, 0.2.1, 0.2.2, 0.2.3, 0.2.4, 0.2.5, 0.2.7, 0.2.8, 0.2.9, 0.3.0, 0.3.1, 0.3.2, 0.3.3, 0.3.4, 0.3.5, 0.3.6, 
0.3.7, 0.3.8, 0.3.9, 0.4.0, 0.4.1, 0.4.2, 0.4.3, 0.4.4, 0.4.5, 0.4.6, 0.4.7, 0.4.8, 0.4.9, 0.4.10, 0.4.11)                                                                                      
No matching distribution found for pipreqs==100
这里很多版本，可以选择其中一个未安装的，建议不要装太旧的
~$ pip install pipreqs==0.4.1
~$ pipreqs --help 查看有没有报错，没有报错就ok
接下来正常操作就不会报错啦
```
### 明确环境依赖

pip list 和 pip freeze 打印出来的依赖都有一个问题，那就是无法明确依赖关系。

当我们想清理某一个包时，不知道哪个是直接依赖哪个是间接依赖。导致环境清理不干净或者清理了不该清除的依赖。

这时就可以使用 pipdeptree 来管理依赖树：

```plain
~$ pip install pipdeptree
......
~$ pipdeptree
...
pipreqs==0.4.1
  - docopt [required: Any, installed: 0.6.2]
  - yarg [required: Any, installed: 0.1.9]
    - requests [required: Any, installed: 2.27.1]
      - certifi [required: >=2017.4.17, installed: 2021.10.8]
      - chardet [required: >=3.0.2,<5, installed: 4.0.0]
      - idna [required: >=2.5,<3, installed: 2.10]
      - urllib3 [required: >=1.21.1,<1.27, installed: 1.26.16]
...
```
这样我们就清楚的知道依赖直接的关系，在依赖清理时就可以避免出现问题。
### 环境依赖治理

如果说我们想卸载 requests 包，直接使用 pip uninstall requests 命令你会发现怎么卸不干净？

```plain
:~$ pipdeptree
setuptools==40.8.0
six==1.12.0
wheel==0.32.3
yarg==0.1.9
  - requests [required: Any, installed: 2.27.1]
    - certifi [required: >=2017.4.17, installed: 2021.10.8]
    - chardet [required: >=3.0.2,<5, installed: 4.0.0]
    - idna [required: >=2.5,<3, installed: 2.10]
    - urllib3 [required: >=1.21.1,<1.27, installed: 1.26.16]
:~$ pip uninstall requests
:~$ pipdeptree
setuptools==40.8.0
six==1.12.0
urllib3==1.26.16
wheel==0.32.3
yarg==0.1.9
  - requests [required: Any, installed: 2.21.0]
发现只是单纯的卸载了requests，它依赖的包并没有被卸载！
```
那么推荐一个工具 pip-autoremove 来做这件事情，下面用这个工具来试试：
```plain
~$ pip install pip-autoremove
...
~$ pip-autoremove requests -y
...
:~$ pipdeptree
six==1.12.0
wheel==0.32.3
yarg==0.1.9
  - requests [required: Any, installed: 2.21.0]
```
你会发现非常好用哈，它会检索到 requests包 和它的相关依赖，然后全部卸载，可以说是非常干净！
### 常见问题

pip install 与 python install 区别

以 requests 为例：

- 当我们用 pip install requests 安装 requests 模块，则会把 requests 依赖的其他库都安装上，不需要在去费力安装依赖的库了。

- 当我们使用 pip setup.py install 安装 requests 模块，需要去手动安装第三方依赖，否则在 import requests 时会出现报错。

## conda

conda是一个支持多语言的包、依赖和环境管理工具，它不仅能管理包，还可以隔离和管理不同Python版本的环境，类似于管理node.js环境的nvm工具。

conda官方一共有两个发行版anaconda和miniconda，anaconda相比miniconda体积更大，预装了许多科学计算的库，很多东西未必会用的到，所以建议使用miniconda。

对于跨语言的或者是本身就整合了各种依赖的环境(比如tenserflow)，再考虑使用conda。

### 安装miniconda

1.首先下载miniconda的安装脚本

    [https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)

2.执行安装脚本

3.一直回车等到出现如下提示并输入yes回车

```plain
Do you accept the license terms? [yes|no]
[no] >>> 
Please answer 'yes' or 'no':'
>>> yes
```
4.指定安装路径
```plain
[/home/uos/miniconda3] >>> 这里的路径可以根据自己情况设定，指定完成回车
我这里就不指定了，使用默认路径
```
5.初始化conda
```plain
by running conda init? [yes|no]
[no] >>> yes 
```
通过简单的操作就可以安装成功了，当打开终端提示符前出现(base)说明进入了默认虚拟环境。
### 取消激活base环境

当miniconda安装完成之后，每次打开终端都会激活其默认的base环境，我们可以通过以下命令禁止激活默认base环境。

```plain
conda config --set auto_activate_base false 
```
### 安装/卸载Python包

当我们想在conda中安装包，可以选择用conda install或者pip install，两者基本相同，但是pip是通过pypi仓库拉取的数据，而conda是通过anaconda.org上拉取的数据。所以说pip的包更全。

以requests为例：

```plain
:~$ conda install requests  安装
:~$ conda uninstall requests  卸载
操作方法和pip几乎一样
```
### 依赖管理

conda 也有和pip freeze类似的依赖管理方式：

为当前环境创建配置文件：

```plain
:~$ conda env export > environment.yaml 
```
根据配置文件复现当前环境：
```plain
:~$ conda env create -f environment.yaml
```
### 环境操作

首先创建一个环境，并激活该环境：

```plain
:~$ conda create -n uos python=3.7 -y  环境名称可以自定义，我这里使用uos
...
:~$ conda activate uos
```

需要注意的是，创建环境之后，一定要 activate 该环境，否则后续的 install 操作还是在 base 环境。
查看已有环境列表：

```plain
:~$ conda env list
# conda environments:
#
base                     /home/uos/miniconda3
uos                   *  /home/uos/miniconda3/envs/uos
```

查看当前环境下的依赖：

```plain
:~$ conda list
# packages in environment at /home/uos/miniconda3/envs/uos:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
_openmp_mutex             5.1                       1_gnu  
ca-certificates           2023.01.10           h06a4308_0  
certifi                   2022.12.7        py37h06a4308_0  
ld_impl_linux-64          2.38                 h1181459_1
...
```

退出环境：

```plain
:~$ conda deactivate
:~$ exit  环境内直接退出
```

### 切换环境技巧

当我们切换环境时，会使用conda activate命令，如果我们想只输入uos可不可以激活环境呢？

当然可以，操作如下：

```plain
:~$ vim ~/.bash_profile
alias uos="conda activate uos"
:~$ source ~/.bash_profile
:~$ uos
此方法适用于环境与环境之间切换
```

### 常用命令

环境相关：

```plain
conda remove -n [env_name] --all  移除环境
conda create --name new_env_name --clone base_env_name  克隆环境
```

日常相关：

```plain
conda search [package_name]  搜索安装包信息
conda update [package_name]  更新包
conda remove [package_name]  删除包
conda clean -t  直接清除被缓存包
conda clean -y -a  直接清除索引缓存、未使用缓存包
```

## 

## pdm

pdm是一个新的Python包管理器，于2021年发布1.0版本，目前最新版为2.7。值得一提的是这款工具的开发者是中国人。为什么选择pdm呢？首先它不是传统的包管理器(pipenv,poetry)需要基于虚拟环境，pdm得益于2018年的一个PEP提案（PEP582，Python local packages directory），完全摒弃了虚拟环境。

PDM 包含如下特性：

1.PEP 582 本地项目库目录，支持安装与运行命令，完全不需要虚拟环境。

2.一个简单且相对快速的依赖解析器，特别是对于大的二进制包发布。

3.兼容 PEP 517 的构建后端，用于构建发布包(源码格式与 wheel 格式)

4.拥有灵活且强大的插件系统（有插件系统直接就拉开一个档次）

5.PEP 621 元数据格式

6.像 pnpm 一样的中心化安装缓存，节省磁盘空间

### 安装

pdm的安装方式有很多种，比如pip、pipx、homebrew等。这里推荐一款安装命令行安装工具，pipx 是安装并运行 Python 终端用户应用（end-user applications）的工具。终端用户应用，其实可以理解为用 Python 编写的命令行工具，可以直接从命令行调用的那种。

```plain
python3 -m pip install --user pipx
```
pipx 需要 Python 3.6 及以上版本，同时必须已经安装好了 pip。
```shell
pipx install pdm
```
如果提示虚拟环境没有被创建需要安装venv，可以通过命令进行安装。
```shell
sudo apt-get install python3-venv
```
安装完成之后再通过pipx命令进行安装pdm。
```plain
:~$ pipx install pdm
  installed package pdm 2.7.0, installed using Python 3.7.3
  These apps are now globally available
    - pdm
done! ✨ 🌟 ✨
```
### 初始化pdm

执行 pdm init 就会开始初始化，初始化的时候，会让你选择项目的一些信息

```plain
:~$ pdm init
Creating a pyproject.toml for PDM...
Please enter the Python interpreter to use
0. /usr/bin/python (2.7)
1. /usr/bin/python3.7m (3.7)
2. /usr/bin/python3.7 (3.7)
3. /usr/bin/python2.7 (2.7)
4. /home/uos/.local/pipx/venvs/pdm/bin/python (3.7)
Please select (0): 2
Using Python interpreter: /usr/bin/python3.7 (3.7)
Using __pypackages__ because non-venv Python is used.
Would you like to create a virtualenv with /usr/bin/python3.7? [y/n] (y): y
Virtualenv is created successfully at /home/uos/.venv
Is the project a library that is installable?
If yes, we will need to ask a few more questions to include the project name and build backend [y/n] (n): y
Project name (uos): 123like
Project version (0.1.0): 
Project description (): 
Which build backend to use?
0. pdm-backend
1. setuptools
2. flit-core
3. hatchling
4. pdm-pep517
Please select (0): 4
License(SPDX name) (MIT): 
Author name (): 
Author email (): 
Python requires('*' to allow any) (>=3.7): 
Changes are written to pyproject.toml.
Found following files from other formats that you may import:
0. /home/uos/requirements.txt (requirements)
1. don't do anything, I will import later.
Please select: 1
```
完成之后，PDM 会将你的选择以 toml 格式写入 pyproject.toml 配置文件中。
```plain
:~$ cat pyproject.toml 
[project]
name = "123like"
version = "0.1.0"
description = ""
authors = [
    {name = "", email = ""},
]
dependencies = []
requires-python = ">=3.7"
readme = "README.md"
license = {text = "MIT"}

[build-system]
requires = ["pdm-pep517>=1.0"]
build-backend = "pdm.pep517.api"
```
### 包操作

安装包和 Poetry 一样，安装使用的是 add 命令

```plain
pdm add requests
```
查看包
```plain
pdm list --graph
```
pdm list 还有两个选项：
–freeze：以 requirements.txt 的格式列出已安装的包

–json：以 json 的格式列出已安装的包，但必须与 --graph 同时使用

要查看某个包的某体详情，直接用 pdm show some_package即可

```plain
pdm show requests
```
删除包
```plain
pmd remove requests
```
更新包
```shell
# 更新所有包
pdm update 
# 更新某个包
pdm update <somepackage>
```
### 项目配置

```plain
pdm config
Site/default configuration (/etc/xdg/pdm/config.toml):
build_isolation = True
cache_dir = /home/uos/.cache/pdm
check_update = True
...
Home configuration (/home/uos/.config/pdm/config.toml):
Project configuration (/home/uos/pdm.toml):
```
pdm config 里面有非常多的配置，想要一一搞清楚的可以去官网查阅：[https://pdm.fming.dev/latest/reference/configuration/](https://pdm.fming.dev/latest/reference/configuration/)
### 运行命令

想要在 pdm 的环境中执行命令或者项目，可以使用 run 命令，若是执行项目时，有诸多参数，可以在 pyproject.toml 配置命令别名。

```plain
:~$ pdm run python main.py 
hello,uos
```
### 命令别名

在 pyproject.toml 添加 [tool.pdm.scripts]可以设置快捷命令别名，若项目的执行有非常多的参数，这种设定别名的方法将很有用 。

```plain
[tool.pdm.scripts]
start = "python main.py"

:~$ pdm run start
hello,uos
```
[tool.pdm.scripts]有两种形式：
```plain
# 第一种
[tool.pdm.scripts]
start = "python main.py"
# 第一种
[tool.pdm.scripts]
start = {cmd = "python main.py"}
```
### 切换 Python 版本

当你在初始化 pdm 项目时，就已经选定了当前的 Python 版本和可用的 Python 版本范围，后面如果想更改，可以使用 use 命令，但版本要受之前设定的版本范围约束。假设允许范围是 python 3.9+，当前使用的是 python 3.10，可以直接切换过去。

```plain
pdm use python3.9  
```
假设允许范围是 python 3.9+，当前使用的是 python 3.10，可以直接切换过去。

### 兼容环境

pdm 足够好用，也足够开放，如果你当前使用的是其他的包管理器，比如 pipenv ，poetry，或者还在用最原始的 requirements.txt ，你也可以很方便的迁移到 pdm 中来：

1.使用 pdm import -f {file} 无需初始化，直接转换

2.执行 pdm init 或者 pdm install 的时候，会自动识别你当前的依赖情况并转换

同样的，你也可以当 pdm 管理的项目，导出为其他方案pyproject.toml 和 pdm.lock是 pdm 的两个核心文件。pdm 做为一个后起之秀，也没有忘本，它支持：

将 pyproject.toml 转成 setup.py

```plain
pdm export -f setuppy -o setup.py
```
将 pdm.lock 转成 requirements.txt
```plain
pdm export -o requirements.txt
```

## venv

venv是Python中自带的一个专门用于管理虚拟环境的模块。

### 创建虚拟环境

```plain
:~$ python3 -m venv uos   uos为虚拟环境名称，可以自定义
```
可以说是非常的快，两三秒就创建成功了！
创建完成之后在环境目录下，可以看到一个pyvenv.cfg的文件，它记录着虚拟环境的基本信息，包括你使用的 Python 的家目录，还有当前虚拟环境的 Python 版本，是否开启使用系统的 site-packages 模块，如果开启了，那么当你就可以直接使用系统中已经装过的第三方模块，但是你在虚拟环境下装的模块就不能被其他地方的程序使用。

```plain
:~/uos$ cat pyvenv.cfg 
home = /usr/bin
include-system-site-packages = false
version = 3.7.3
```
如果你的系统里有多个Python3环境，那么在创建时指明清楚版本号就可以了。
```plain
:~$ python3.9 -m venv [venv_dir]
```
### 进入虚拟环境

首先我们进入到创建好的虚拟环境目录，通过source进入虚拟环境：

```plain
:~/uos$ source bin/activate
(uos) uos@uos-PC:~/uos$
命令行前有创建的虚拟环境名称说明就已进入
```
### 退出虚拟环境

```plain
:~$deactivate
```
### 总结

venv是 Python3 中自带的虚拟环境管理工具，不需要额外安装，功能简单，用法也简单。但是它不能像 poetry 和 pipenv 用于项目的管理，因此 venv 建议只做了解，在一些简单的场景中可以使用，如果是复杂的项目中，可以直接上 poetry 和 pipenv。 

## virtualenv

...

### virtualenvwrapper

...

## pyenv

...

## pipenv

...

## poetry







