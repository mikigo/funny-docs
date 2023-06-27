# HttpRunner—2小时入门版

## 一、简介

接口测试很多同学用 `Postman`、`Jmeter` 来做，用起来也挺简单的，但是接口用例多了之后就发现不好管理维护，要落地到公司级 CI 项目就有点难搞了；

稍微有点技术能力的同学更愿意直接用 `requests` 来做接口自动化，但是大多用 `requests` 来做的接口自动化项目，在工程化方面都做得不太好，与其说是接口自动化项目，不如说是接口脚本的集中存放，没有体系化的框架结构设计，因此在大型 CI 项目中落地也显得不太够用，维护人员除了忙于接口脚本的维护，还要投入大量时间做新功能和修复代码中的 Bug。

想要轻松快速的落地接口自动化，又不想自己去折腾，我个人还是推荐 `HttpRunner`，只需要写写配置文件就把活干完了；

## 二、安装

系统环境：`deepin` / `UOS`

```console
sudo bash -c "$(curl -ksSL https://httprunner.com/script/install.sh)"
```

注意，使用 `sudo` 安装，不然命令行工具无法写入系统环境变量。

装完之后会有一些版本、命令行参数的输出，说明安装成功。

## 创建项目

```shell
hrp startproject funny-api-autotest
```

这里会使用 `venv` 创建一个虚拟，有可能报错需要安装 `python3-venv`；

不要慌，我们来修复一下环境：

```shell
# 安装依赖
sudo apt install python3-pip
# 安装venv
sudo apt install python3-venv
# 把之前创建失败的虚拟环境删掉
cd ~/.hrp/
rm -rf venv
# 重新创建一个
python3 -m venv venv
# 激活虚拟环境
source ~/.hrp/venv/bin/activate
# 把pip更新一下
pip install --upgrade pip setuptools wheel
# 安装依赖funppy
pip install funppy
```

如果不出意外，环境就安装好了；



