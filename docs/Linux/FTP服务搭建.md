# FTP服务搭建

## 安装

```shell
sudo apt install vsftpd
```

## 配置用户

添加用户组

```shell
sudo groupadd ftpgroup
```

配置 `FTP` 访问用户 `uos`

```shell
sudo useradd -g ftpgroup -M -s /bin/bash uos
```

配置 `FTP` 访问密码

```shell
sudo passwd uos
```

之后输入 2 次密码即可；

## 修改配置项

```shell
sudo vim /etc/vsftpd.conf
```

配置以下内容：

```shell
# 文件编码
utf8_filesystem=YES

# 开启匿名访问
anonymous_enable=YES

# 匿名用户无密码
no_anon_password=YES

# 限定匿名用户目录，路径可以自定义
anon_root=/home/$USER/ftp

# 可写
write_enable=YES

# 匿名上传
anon_upload_enable=YES

# 匿名可写文件夹
anon_mkdir_write_enable=YES

# 其他用户匿名可写
anon_other_write_enable=YES

# 匿名用户创建文件时所得到的初始权限
# 022 新建的目录权限为755，新建的文件权限为644
anon_umask=022

# 本地用户
chroot_local_user=YES

# 用户列表
chroot_list_enable=YES

# 用户列表文件
chroot_list_file=/etc/vsftpd.chroot_list

# 权限用户目录，路径可以自定义
local_root=/ftp/ftp
```

配置用户列表文件：

```shell
sudo vim /etc/vsftpd.chroot_list
```

写入

> uos

## 创建FTP目录

```shell
sudo mkdir -p /ftp/ftp # 权限访问目录
sudo mkdir -p /home/$USER/ftp # 匿名访问目录
```

修改目录权限

```shell
sudo chmod -R 777 /ftp/ftp
sudo chmod -R 777 /home/$USER/ftp
```

## 重启服务

```shell
sudo systemctl restart vsftpd.service
sudo systemctl status vsftpd.service
```

## SFTP

```shell
# Match Group mysftp 
# 告诉sshd进程，mysftp用户组中的用户适用下面的限制；

# 限制sftp的活动目录在其sftp目录；
ChrootDirectory /data/sftp  
# 防止用户执行他们自己自定义的命令，限制用户命令执行上下文为sftp；
ForceCommand internal-sftp 
# 禁止X11转发；
X11Forwarding no 
# 禁止tcp转发；
AllowTcpForwarding no 
```

