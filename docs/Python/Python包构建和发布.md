# Python包构建和发布

## 1、必要的文件

除了你的源代码以外，你还需要准备以下文件；

### LICENSE

开源协议文件

这里以我的项目用到的开源协议举例：

https://github.com/funny-dream/pdocr-rpc/blob/main/LICENSE

### README

介绍这个包的安装及使用，理论上你可以写任何东西在上面，主要让别人全方位了解这个包的使用；

### pyproject.toml

网络上大多关于 Python 打包使用的都是 `setup.py`，最新最流行的是使用 `pyproject.toml`，`pypi` 官方也推荐使用它；

相比于`setup.py`，`pyproject.toml` 的描述更为精细，但也更为繁琐，如果你是高定玩家，当然首选 `pyproject.toml` ；

当然，常用的几个东西都差不多，下面就以我的项目举例简单介绍一下：https://github.com/funny-dream/pdocr-rpc/blob/main/pyproject.toml

里面主要包含这些内容：

#### build-system

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

构建系统

#### project

```toml
[project]
name = "pdocr-rpc"
authors = [
  { name="mikigo", email="1964191531@qq.com" },
]
description = "PaddleOCR-RPC"
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
]

dependencies = [
    "pyscreenshot;sys_platform == 'linux'",
    "pillow;sys_platform == 'win32'",
]

```

这里面就是一些基本信息，你可以按照自己的实际情况修改；

注意：

（1）`classifiers` 里面 `License` 字段要和项目的开源协议一致；在这里列出了所有的开源协议应该怎么写：https://pypi.org/classifiers/

（2）`dependencies` 是你项目的依赖，别人使用 pip 安装的时候会同时安装上这些依赖；

注意这里如果有一些条件，比如有些包有版本的、操作系统、Python版本的限制，必须要按照规范写：https://peps.python.org/pep-0508/

（3）可选依赖

```toml
[project.optional-dependencies]
test = [
    "pytest",
]
doc = ["mkdocs-material"]
```

这些是可选的，安装的时候可以这样进行安装：

```shell
pip install pdocr-rpc[test]
```

这样就会安装 `pytest`

（4）urls

```toml
[project.urls]
Source = "https://github.com/funny-dream/pdocr-rpc"
Documentation = "https://funny-dream.github.io/pdocr-rpc"
```

这个在 `pypi` 的网页端能展示，别人可以通过那里跳转的你的文档或源码页面；

（5）version

```toml
[tool.hatch.version]
path = "allure_custom/__version__.py"
```

用一个 `__version__.py` 指定版本是比较优雅的方法；

```python
__title__ = "allure_custom"
__version__ = "2023.6.26"
```



关于 `project` 下的详细内容及规范，请查看：https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata

## 2、打包

安装打包工具：

```shell
sudo pip3 install build
```

打包：

```shell
python3 -m build
```

完成后应生成两个目录中的文件：`dist`

```
dist/
├── xxx.whl
└── xxx.tar.gz
```

## 3、发布

首先你需要注册一个  pypi 的账号：https://pypi.org/account/register/

安装发布工具：

```shell
sudo pip3 install twine
```

发布：

```shell
twine upload dist/*
```

输入你的账号密码即可发布到 pypi，以后每次发布包记得更新版本；

