---
counter: True
---

# 配置 Python 源的几种方法

```shell
# ==================================
# Author : mikigo
# ==================================
```


## （1）临时添加三方源

```shell
pip3 install funnylog -i https://pypi.tuna.tsinghua.edu.cn/simple
```

如果不小心添加了多个，就像这样：

```shell
pip3 install xxx -i yyyy -i zzzz
```

只有最后一个 -i 指定的三方源生效；

## （2）requirements.txt 临时添加三方源

```shell
# requirements.txt
-i https://pypi.tuna.tsinghua.edu.cn/simple

funnylog
...
```

## （3）命令行永久配置

- 适用于 `pip3 install` 的安装方式（**普通用户**）：

```shell
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

- 适用于 `sudo pip3 install` 的安装方式（**root用户**）：

```shell
sudo pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

可以再次执行再添加一个:

```shell
pip3 config set global.extra-index-url https://pypi.douban.com/simple/
```

注意 `global.extra-index-url` 里面和上面不同；

## （4）修改配置文件永久配置

- 适用于 `pip3 install` 的安装方式（**普通用户**）：

```shell
vi ~/.config/pip/pip.conf
```

配置如下：

```config
[global]
index-url = https://pypi.douban.com/simple/
extra-index-url = https://pypi.tuna.tsinghua.edu.cn/simple
extra-index-url = https://mirrors.aliyun.com/pypi/simple/
```

- 适用于 `sudo pip3 install` 的安装方式（**root用户**）：

```shell
sudo vi /root/.config/pip/pip.conf
```

配置如下：

```shell
[global]
index-url = https://pypi.douban.com/simple/
extra-index-url = https://pypi.tuna.tsinghua.edu.cn/simple
extra-index-url = https://mirrors.aliyun.com/pypi/simple/
```

- **全局配置**

```shell
vi /etc/pip.conf
```

配置如下：

```shell
[global]
index-url = https://pypi.douban.com/simple/
extra-index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

## （5）作用域

- 临时添加的方式，只在本次操作有效（不区分普通用户、root用户、全局配置）；
- 普通用户的配置方式，只在普通用户权限下生效，就是只有使用 `pip3 install` 生效；
- root用户的配置方式，只在root用户权限下生效，就是只有使用 `sudo pip3 install` 生效；
- 全局配置方式，所有情况下均生效；


## （6）常用的几个三方源

```shell
# 清华
https://pypi.tuna.tsinghua.edu.cn/simple/
# 阿里
https://mirrors.aliyun.com/pypi/simple/
# 中国科技大学
https://pypi.mirrors.ustc.edu.cn/simple/
# 华中科技大学
https://pypi.hustunique.com/simple/
# 上海交通大学
https://mirror.sjtu.edu.cn/pypi/web/simple/
# 豆瓣
https://pypi.douban.com/simple/
```

-------------------------------------

补充小知识，pip 下载安装超时设置：

```shell
pip3 config set global.timeout 10000
```

------------------------------------

吐槽一下阿里的镜像，更新相当不及时，我个人不建议使用哈。
