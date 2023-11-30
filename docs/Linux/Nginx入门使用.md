# Nginx入门使用

## 安装

```shell
sudo apt install nginx
```

安装之后 `/var/www/html` 就可以作为默认的 `http` 服务使用了；

## 配置

配置文件路径：`/etc/nginx/nginx.conf`

```shell
sudo vim /etc/nginx/nginx.conf
```

默认配置如下：

```shell
# 全局配置
user mikigo;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

# events配置
events {
        worker_connections 768;
        # multi_accept on;
}

# http配置
http {
		# http全局配置
        ##
        # Basic Settings
        ##

        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        # server_tokens off;

        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        ##
        # SSL Settings
        ##

        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
        ssl_prefer_server_ciphers on;

        ##
        # Logging Settings
        ##

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        ##
        # Gzip Settings
        ##

        gzip on;

        # gzip_vary on;
        # gzip_proxied any;
        # gzip_comp_level 6;
        # gzip_buffers 16 8k;
        # gzip_http_version 1.1;
        # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

        ##
        # Virtual Host Configs
        ##

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
        
        autoindex on;
        autoindex_exact_size on;
        autoindex_localtime on;
        charset utf-8;
        # server配置，可以有多个server
        server {
                listen          8001;
                server_name     localhost;

                location / {
                        root /home/mikigo/Desktop/share;
                        index index.html;
                }
        }
}
```

一共由三部分组成，分别为 全局配置、`events`  配置和 `http` 配置；

在 `http` 中，又包含 `http` 全局配置、多个 `server` 配置，每个 `server` 中，可以包含 `server` 全局配置和多个 `location` 配置；

下面展开讲。

## 全局配置

```shell
# 全局配置
user mikigo;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;
```

`user`  ：用于指定运行 `nginx` 服务的用户和用户组；将 `user` 注释掉或者配置成 `nobady` 表示所有用户都可以运行；

`worker_processes` ：指定工作线程数，`auto` 表示自动模式；

`pid`：指定 `pid` 文件存放的路径

## events

```shell
# events配置
events {
        worker_connections 768;
        # multi_accept on;
}
```

`worker_connections`：设置允许每一个 `worker process` 同时开启的最大连接数；

`multi_accept`: `on` 表示一个工作进程可以同时接受所有的新连接，`off` 表示一个工作进程只能同时接受一个新的连接，默认是 `off`；

## http

```shell
# http配置
http {
		# http全局配置
        ##
        # Basic Settings
        ##
		# 开启关闭sendfile方式传输文件
        sendfile on;
        # 此选项允许或禁止使用socke的TCP_CORK的选项，此选项仅在使用sendfile的时候使用
        tcp_nopush on;
        tcp_nodelay on;
        # 长连接超时时间，单位是秒
        keepalive_timeout 65;
        types_hash_max_size 2048;
        # server_tokens off;

        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;
        
		# 文件扩展名与文件类型映射表
        include /etc/nginx/mime.types;
        # 默认文件类型
        default_type application/octet-stream;

        ##
        # SSL Settings
        ##

        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
        ssl_prefer_server_ciphers on;

        ##
        # Logging Settings
        ##
		# 日志记录文件
        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        ##
        # Gzip Settings
        ##
		# 开启gzip压缩输出
        gzip on;
		# gzip 的一些配置项
        # gzip_vary on;
        # gzip_proxied any;
        # gzip_comp_level 6;
        # gzip_buffers 16 8k;
        # gzip_http_version 1.1;
        # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

        ##
        # Virtual Host Configs
        ##

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
        # 开启目录列表访问，合适下载服务器，默认关闭
        autoindex on;
        # 文件服务器文件大小
        autoindex_exact_size on;
        # 文件服务器文件时间
        autoindex_localtime on;
        #默认编码
        charset utf-8;
        
        # server配置，可以有多个server
        server {
                listen          8001;
                server_name     localhost;

                location / {
                        root /home/mikigo/Desktop/share;
                        index index.html;
                }
        }
}
```

默认的 80 端口的服务是不用配置的；

访问：`IP:80`，实际访问的路径为：`/var/www/html`

访问：`IP:8001`，实际访问的路径为：`/home/mikigo/Desktop/share`
