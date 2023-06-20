# Linux 上 sudo 免密

```shell
sudo visudo
```

或者

```shell
sudo vim /etc/sudoers
```

找到

```shell
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
```

加个 NOPASSWD: 就好了；

```shell
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) NOPASSWD: ALL
```

