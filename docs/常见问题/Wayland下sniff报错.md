# Wayland下sniff命令报错~/.Xauthorty文件不存在

```shell
# ==================================
# Author : mikigo
# ==================================
```

/faq/sniff_error.png)

根据 Xlib.xauth 源代码里面这里：

```python
class Xauthority:
    def __init__(self, filename = None):
        if filename is None:
            filename = os.environ.get('XAUTHORITY')

        if filename is None:
            try:
                filename = os.path.join(os.environ['HOME'], '.Xauthority')
            except KeyError:
                raise error.XauthError(
                    '$HOME not set, cannot find ~/.Xauthority')

        try:
            raw = open(filename, 'rb').read()
        except OSError as err:
            raise error.XauthError('~/.Xauthority: %s' % err)

        self.entries = []
```



是因为读文件 `filename` 的时候报错，`filename` 要么从环境变量 `XAUTHORITY` 里面拿，要么就赋值 `~/.Xauthority`，而咱们系统中 `~/.Xauthority` 文件是存在的，那么肯定就是环境变量里面 `XAUTHORITY` 的值有问题；
查看一下：

/faq/sniff_error2.png)


环境变量里面有 `XAUTHORITY`，但是值为空；

所以这就是问题，`filename` 拿到一个空串，`open` 读肯定会报 `OSError`；

解决方法，在 `sniff` 的代码里面把 `XAUTHORITY=~/.Xauthority` 这个环境变量加上理论上就行了；

```
import os
os.environ["XAUTHORITY"] = "$HOME/.Xauthority"
```

再执行 `sniff` 就不会报错啦；