
# Httpx

```shell
# =============================
# Author : mikigo
# =============================
```

## 1、简介

虽然 Requests 基本已经可以解决大部分问题，但仍然有少部分问题无法解决，比如：HTTP/2（Requests 只支持HTTP/1.1）、异步请求等，这就需要用到 httpx；

httpx 号称下一代 HTTP 客户端，最开始是为了解决 Requests 不支持异步请求的问题，工程名称就叫：requests-async，后面整体迁移到 httpx 仓库中。

由于 httpx 从一开始就是基于 Requests 来搞的，所以它提供的接口几乎和 Requests 保持一致，这对于我们使用来说就简单多了。

## 2、安装

系统环境：deepin

```console
pip3 install httpx
```

它还提供命令行工具：

```console
pip3 install 'httpx[cli]'
```

我一般不咋习惯用命令行做接口请求，所以基本都不装这玩意儿。

## 3、简单的例子

前面说了 httpx 和 Requests 提供的接口几乎一致，咱们就用 Requests 教程里面的例子；

### 3.1、GET请求

```python
import httpx

r = httpx.get("https://www.baidu.com")
print(r.status_code)
print(r.text)
```

执行后终端输出：

```console
200
<html>
<head>
        <script>
                location.replace(location.href.replace("https://","http://"));
        </script>
</head>
<body>
        <noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
</body>
</html>
```

### 3.2、POST请求

```python
import httpx

r = httpx.post('https://httpbin.org/post', data={'key': 'value'})
print(r.status_code)
print(r.text)
```

执行后终端输出：

```console
200
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key": "value"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "9", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-httpx/0.23.3", 
    "X-Amzn-Trace-Id": "Root=1-642f820c-019ccf8938faee564386038e"
  }, 
  "json": null, 
  "origin": "110.191.179.216", 
  "url": "https://httpbin.org/post"
}
```

你看，简直是一毛一样。

行啦，都一样咱们就不聊了，后面重点讲讲不一样的。

## 4、异步请求

异步是一种并发方式，也就是通常说的“协程”，比多线程效率高很多；

httpx 的异步请求主要依赖于标准库 asyncio，使用 async 和 await 关键词；

```python
import asyncio
import httpx

async def my_get():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://www.baidu.com")
        print(r.text)

if __name__ == '__main__':
    asyncio.run(my_get())
```

client 对象你可以理解为 Requests 里面的 Session 对象。

## 5、HTTP/2

老实讲 HTTP/2 的网站我还没机会爬过，所以我这里还不太好找例子；

如果你在不小心遇到了也别慌，只需要加一个参数就好了；

```python
import asyncio
import httpx

async def my_get():
    async with httpx.AsyncClient(http2=True) as client:
        r = await client.get("https://www.xxxxxx.com")
        print(r.text)

if __name__ == '__main__':
    asyncio.run(my_get())
```

在 `httpx.AsyncClient()` 里面，默认参数: 

```python
class AsyncClient:
    def __init__(
        self,
		...
        http1: bool = True,
        http2: bool = False,
		...
    ):
        pass  # 省略其他源码
```

也就是说默认是开启的 http1，所以只需要在实例化 client 对象的时候，传入参数 `http2=True` 即可；
