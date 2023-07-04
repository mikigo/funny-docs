# Linux 上远程桌面 VNC 服务配置

## 服务端

一键部署脚本：

```shell
#!/bin/bash
# 安装VNC
sudo apt install x11vnc -y
# 密码设置为1
sudo x11vnc -storepasswd 1 /etc/x11vnc.pass
# 配置开机自启服务
vnc_connect(){
sudo bash -c 'cat << EOF > "/lib/systemd/system/x11vnc.service"

[Unit]
Description=Start x11vnc at startup
After=multi-user.target
[Service]
Type=simple
ExecStart=/usr/bin/x11vnc -auth guess -forever -loop -noxdamage -repeat -rfbauth /etc/x11vnc.pass -rfbport 5900 -shared
[Install]
WantedBy=multi-user.target
EOF'
}

vnc_connect
sudo chmod 755 /lib/systemd/system/x11vnc.service
sudo chown root:root /lib/systemd/system/x11vnc.service
# 开机自启
sudo systemctl enable x11vnc.service
# 启动服务
sudo systemctl daemon-reload
sudo systemctl start x11vnc.service
```

## 客户端

```shell
#安装tigervnc-viewer
sudo apt install tigervnc-viewer
```

客户端打开 `tigervnc-viewer`，配置要远程连接服务器地址，点击 `Connect`，输入密码即可。
