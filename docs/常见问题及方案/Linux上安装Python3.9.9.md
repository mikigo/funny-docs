# Linux 上安装 Python 3.9.9

```shell
#!/bin/bash
# 刷新源
sudo apt update
# 装依赖
sudo apt install -y zlib1g-dev libbz2-dev libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev tk-dev libgdbm-dev libdb-dev libpcap-dev xz-utils libexpat1-dev liblzma-dev libffi-dev libc6-dev
# 下载源码
wget https://cdn.npm.taobao.org/dist/python/3.9.9/Python-3.9.9.tgz
# 解压
tar -xzf Python-3.9.9.tgz
# 放在/usr/local/share/下
sudo mv  Python-3.9.9 /usr/local/share/
# 编译
cd  /usr/local/share/Python-3.9.9/
./configure --prefix=/usr/local/python3.9
# 设置优化选项--enable-optimizations
# ./configure --prefix=/usr/local/python3.9 --enable-optimizations
make -j4
sudo make install
# 设置软连接
sudo ln -s /usr/local/python3.9/bin/python3.9 /usr/bin/python3.9
sudo ln -s /usr/local/python3.9/bin/python3.9-config /usr/bin/python3.9-config
```

-------------------------------------------

