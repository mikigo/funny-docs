# Error: ENOSPC: System limit for number of file watchers reached

```shell
# ==================================
# Author : mikigo
# ==================================
```


报错的原始输出：

```shell
node:internal/errors:490
    ErrorCaptureStackTrace(err);
    ^

Error: ENOSPC: System limit for number of file watchers reached, watch '/home/uos/github/muyi-frontend/.env.development'
    at FSWatcher.<computed> (node:internal/fs/watchers:247:19)
    at Object.watch (node:fs:2343:34)
    at createFsWatchInstance (file:///home/uos/github/muyi-frontend/node_modules/.pnpm/vite@4.3.9_@types+node@20.3.1_sass@1.63.6_terser@5.18.1/node_modules/vite/dist/node/chunks/dep-e8f070e8.js:50470:17)
    at setFsWatchListener (file:///home/uos/github/muyi-frontend/node_modules/.pnpm/vite@4.3.9_@types+node@20.3.1_sass@1.63.6_terser@5.18.1/node_modules/vite/dist/node/chunks/dep-e8f070e8.js:50517:15)
    at NodeFsHandler._watchWithNodeFs (file:///home/uos/github/muyi-frontend/node_modules/.pnpm/vite@4.3.9_@types+node@20.3.1_sass@1.63.6_terser@5.18.1/node_modules/vite/dist/node/chunks/dep-e8f070e8.js:50672:14)
    at NodeFsHandler._handleFile (file:///home/uos/github/muyi-frontend/node_modules/.pnpm/vite@4.3.9_@types+node@20.3.1_sass@1.63.6_terser@5.18.1/node_modules/vite/dist/node/chunks/dep-e8f070e8.js:50736:23)
    at NodeFsHandler._addToNodeFs (file:///home/uos/github/muyi-frontend/node_modules/.pnpm/vite@4.3.9_@types+node@20.3.1_sass@1.63.6_terser@5.18.1/node_modules/vite/dist/node/chunks/dep-e8f070e8.js:50978:21)
Emitted 'error' event on FSWatcher instance at:
    at FSWatcher._handleError (file:///home/uos/github/muyi-frontend/node_modules/.pnpm/vite@4.3.9_@types+node@20.3.1_sass@1.63.6_terser@5.18.1/node_modules/vite/dist/node/chunks/dep-e8f070e8.js:52169:10)
    at NodeFsHandler._addToNodeFs (file:///home/uos/github/muyi-frontend/node_modules/.pnpm/vite@4.3.9_@types+node@20.3.1_sass@1.63.6_terser@5.18.1/node_modules/vite/dist/node/chunks/dep-e8f070e8.js:50986:18) {
  errno: -28,
  syscall: 'watch',
  code: 'ENOSPC',
  path: '/home/uos/github/muyi-frontend/.env.development',
  filename: '/home/uos/github/muyi-frontend/.env.development'
}

```

达到文件观察者数量的系统限制；

错误产生的原因是负责监控 Linux 文件系统的 `inotify` 程序达到了系统默认的限制上限；

`inotify` 提供了一种监控文件系统（基于 `inode` 的）事件的机制，可以监控文件系统的变化如文件修改、新增、删除等，并可以将相应的事件通知给应用程序。

查看 `inotify` 在内核中的默认配置

```shell
uos@uos-PC:~$ sudo sysctl fs.inotify
fs.inotify.max_queued_events = 16384
fs.inotify.max_user_instances = 128
fs.inotify.max_user_watches = 8192
```

**解决方法**

临时解决：

```shell
sudo sysctl fs.inotify.max_user_watches=100000
```

永久解决：

```shell
echo fs.inotify.max_user_watches=100000 | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```
