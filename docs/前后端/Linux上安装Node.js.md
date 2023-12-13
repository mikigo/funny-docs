# Linux 上安装 Node.js

在官网下载：https://nodejs.cn/download/current/

以下代码可以直接复制下来，一键执行；

```shell
# 定义下载版本
node_version=v18.16.1

# 定义/opt目录下node目录的名称，以兼容多个node版本
opt_node_dir="node${node_version}"

# 下载node包
wget https://cdn.npmmirror.com/binaries/node/${node_version}/node-${node_version}-linux-x64.tar.xz

# 解压安装包
tar -xvJf node-${node_version}-linux-x64.tar.xz

# 放到/opt目录下
sudo rm -rf /opt/${opt_node_dir}
sudo mv node-${node_version}-linux-x64 /opt/${opt_node_dir}

# 创建npm、node链接到系统目录
sudo rm -rf /usr/local/bin/npm; sudo ln -s /opt/${opt_node_dir}/bin/npm   /usr/local/bin/npm
sudo rm -rf /usr/local/bin/node; sudo ln -s /opt/${opt_node_dir}/bin/node   /usr/local/bin/node

# 设置淘宝镜像源
npm config set registry https://registry.npm.taobao.org

# 安装pnpm
npm install -g pnpm

# 创建pnpm链接到系统目录
sudo rm -rf /usr/local/bin/pnpm; sudo ln -s /opt/${opt_node_dir}/bin/pnpm /usr/local/bin/pnpm
sudo rm -rf /usr/local/bin/pnpx; sudo ln -s /opt/${opt_node_dir}/bin/pnpx /usr/local/bin/pnpx
```

安装完之后查看版本，没报错就说明安装好了；

```shell
node -v
npm -v
pnpm -v
```





