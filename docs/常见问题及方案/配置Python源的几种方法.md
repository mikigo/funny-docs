# 配置Python源的几种方法

## （1）临时添加三方源

```shell
pip3 install funnylog -i https://pypi.tuna.tsinghua.edu.cn/simple
```

如果想临时添加多个，后面可以加多个 -i

```shell
pip3 install xxx -i yyyy -i zzzz
```

## （2）requirements.txt 添加三方源

```shell
# requirements.txt
-i https://pypi.tuna.tsinghua.edu.cn/simple
-i https://pypi.douban.com/simple/

funnylog
...
```

### （3）命令行永久配置

- 适用于 `pip3 install` 的安装方式：

```shell
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

- 适用于 `sudo pip3 install` 的安装方式：

```shell
sudo pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

可以多次执行添加多个:

```shell
pip3 config set global.extra-index-url https://pypi.douban.com/simple/
pip3 config set global.extra-index-url https://mirrors.aliyun.com/pypi/simple/
```

注意 `global.extra-index-url` 里面和上面不同；

## （4）修改配置文件永久配置

- 适用于 `pip3 install` 的安装方式：

```shell
vi ~/.config/pip/pip.conf
```

配置如下：

```config
[global]
index-url = https://pypi.douban.com/simple/
extra-index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

- 适用于 `sudo pip3 install` 的安装方式：

```shell
sudo vi /root/.config/pip/pip.conf
```

配置如下：

```shell
[global]
index-url = https://pypi.douban.com/simple/
extra-index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

## （5）常用的几个三方源

```shell
# 清华
https://pypi.tuna.tsinghua.edu.cn/simple/
# 阿里云
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
