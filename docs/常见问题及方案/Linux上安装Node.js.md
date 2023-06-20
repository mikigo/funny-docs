# Linux 上安装 Node.js

【方法一】

在官网下载：https://nodejs.cn/download/current/

建议选择最新的 `LTS` 版本；

下载下来加压到 `/opt` 目录下：

```shell
ln -s /opt/nodejs/bin/npm   /usr/bin/npm
ln -s /opt/nodejs/bin/node   /usr/bin/node
```

【方法二】2、

`Node.js LTS (v18.x)`:

```
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - &&\
sudo apt-get install -y nodejs
```

安装完之后查看版本，没报错就说明安装好了；

```shell
mikigo@mikigo-PC:~$ node -v
v16.18.1
mikigo@mikigo-PC:~$ npm -v
8.19.2
```

---------------------------------------
