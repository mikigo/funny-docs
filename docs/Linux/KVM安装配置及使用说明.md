# KVM安装配置及使用说明

```shell
# =============================
# Author : mikigo
# =============================
```

## 一、安装 `KVM`

```shell
sudo apt install -y libvirt0 libvirt-daemon qemu virt-manager bridge-utils libvirt-clients python-libvirt qemu-efi uml-utilities virtinst qemu-system
```
## 二、命令安装镜像
### 1、创建存储卷

```shell
mkdir -p work/kvm;qemu-img create -f qcow2 /home/uos/work/kvm/autotest1.qcow2 80G
```
### 2、创建虚拟机

```shell
virt-install \
--name autotest1 \
--memory 2048 \
--vcpus 1 \
--disk /home/uos/work/kvm/autotest1.qcow2,device=disk,bus=virtio \
--os-type=linux \
--os-variant debian10 \
--graphics spice \
--noreboot \
--boot hd \
--cdrom  "/home/uos/Desktop/test.iso" \
--connect qemu:///system \
--network type=direct,source=enp5s0f0,source_mode=bridge
```

## 三、配置远程管理

### 1、增加 `libvirtd` 用户组

```shell
groupadd libvirtd
```
### 2、设置用户到组

```shell
sudo usermod -a -G libvirtd $USER
```
### 3、设置启动libvirtd服务的用户组

```shell
sudo vi /etc/libvirt/libvirtd.conf
```
在尾行写入
```shell
unix_sock_group = "libvirtd"
```

### 4、增加权限启动配置

```shell
sudo vi /etc/polkit-1/localauthority/50-local.d/50-org.libvirtd-group-access.pkla
```
写入
```shell
[libvirtd group Management Access]
Identity=unix-group:libvirtd
Action=org.libvirt.unix.manage
ResultAny=yes
ResultInactive=yes
ResultActive=yes
```
### 5、重启服务

```shell
sudo service libvirtd restart
```

## 四、常见问题

**1、Requested operation is not valid: network 'default' is not active**

解决方案：

```shell
sudo virsh net-start default
sudo virsh net-autostart default
```
