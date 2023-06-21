# Linux 上远程桌面 VNC 服务配置

## 服务端

```shell
# 安装vnc server
sudo apt install x11vnc vnc4server -y;
# 配置服务显示、端口等
sudo x11vnc -display :0 -auth /var/run/lightdm/root/:0 -forever -bg -o /var/log/x11vnc.log -rfbauth /etc/x11vnc.pass -shared -noxdamage -xrandr "resize" -rfbport 5900;
# 配置访问密码
sudo x11vnc -storepasswd 1 /etc/x11vnc.pass;
```

## 客户端

```shell
#安装tigervnc-viewer
sudo apt install tigervnc-viewer
```

客户端打开 `tigervnc-viewer`，配置要远程连接服务器地址，点击 `Connect`，输入密码即可。
