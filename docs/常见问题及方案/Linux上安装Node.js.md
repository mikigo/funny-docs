# Linux 上安装 Node.js

【方法一】

在官网下载：https://nodejs.cn/download/current/

建议选择最新的 `LTS` 版本；

下载下来加压到 `/opt` 目录下：

```shell
sudo ln -s /opt/node/bin/npm   /usr/bin/npm
sudo ln -s /opt/node/bin/node   /usr/bin/node
```

【方法二】

**Node.js v20.x**

```shell
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

**Node.js v19.x**

```shell
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash -
sudo apt install -y nodejs
```

**Node.js v18.x**

```shell
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
```

**Node.js v16.x**

```shell
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt install -y nodejs
```

**Node.js LTS (v18.x)**

```shell
# 下载deb源，并刷新
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
# apt 安装nodejs npm
sudo apt install -y nodejs
```

**Node.js Current (v20.x)**

```shell
curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -
sudo apt install -y nodejs
```

我个人推荐**【方法一】**

安装完之后查看版本，没报错就说明安装好了；

```shell
mikigo@mikigo-PC:~$ node -v
v10.24.0
mikigo@mikigo-PC:~$ npm -v
5.8.0
```

---------------------------------------
