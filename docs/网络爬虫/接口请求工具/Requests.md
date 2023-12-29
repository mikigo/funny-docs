
# Requests

```shell
# =============================
# Author : mikigo
# =============================
```

## 1、简介

Requests 是 Python 最久负盛名的 HTTP 库，没有之一；K 神（Kenneth Reitz）的 for humans 系列中最有名的一个；

![](../../img/spider/k.png)

做爬虫、数据分析、接口自动化会经常用到它，非常多有名的 Python 库依赖于 Requests 提供基础能力，比如：httpx（支持异步的 HTTP 库）、locust（性能[负载]测试框架）、HttpRunner（接口自动化框架）等等，都是基于 Requests 构建起来的。

有人甚至建议将 Requests 库合入 Python 标准库发布。只要你想做 HTTP 请求，你肯定会想到 Requests。

Requests 特点：简单、简洁、优雅。

## 2、安装

系统环境：deepin

```console
pip3 install requests

```

## 3、请求

### 3.1、导入

```python
import requests
```

所有的功能都在 requests 这个名称空间下。

### 3.2、GET 请求

```python
r = requests.get("https://www.baidu.com")
print(r.status_code)
print(r.text)
```

终端打印：

```console
200
<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equ ...... # 省略
```

### 3.3、POST 请求

`https://httpbin.org` 是 K 神的一个简单的 HTTP 服务，主要用于试用 requests 里面的一些功能，方便理解； 

```python
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r.status_code)
print(r.text)
```

终端打印：

```python
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
    "User-Agent": "python-requests/2.28.1", 
    "X-Amzn-Trace-Id": "Root=1-642aa9b9-259b189c1acb1e114a5d6bc7"
  }, 
  "json": null, 
  "origin": "110.191.179.216", 
  "url": "https://httpbin.org/post"
}
```

### 3.4、其他请求

其他请求方式不常用，如下：

```python
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')
```

### 3.5、请求头（headers）

请求头通常会加 UA（user agent），这个主要是模仿浏览器的行为，比如模仿使用 Firefox 浏览器：

```python
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"
}

requests.get(url, headers=headers)
requests.post(url, headers=headers)
```

### 3.6、参数

(1) get 请求参数

get 请求的参数可以直接在url后面加参数，`url?key1=value1&key2=value2`，即 url 后面加问号，然后紧接着多个参数的键和值，多个键值之间用 & 符号链接；

这种方式简单是简单，但是参数多了之后，url 会变得很长，看起来胀眼睛，为了更好的可读性，requests 支持这样传递 get 请求的参数：

```python
params = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=params)
```

通过打印 r.url 你会发现，实际上也是给你转换成了前面那种 & 连接的方式；

（2）post 请求参数

post 请求参数一般是通过data参数传递，通常 data 是一个字典形式：

```python
data = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('https://httpbin.org/post', data=data)
print(r.text)
```

执行后终端输出：

```console
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.28.1", 
    "X-Amzn-Trace-Id": "Root=1-642e7884-7f20428d523e7fda1da61f1a"
  }, 
  "json": null, 
  "origin": "110.191.179.216", 
  "url": "https://httpbin.org/post"
}
```

如果你拿到的参数，是一个 json 格式，可以直接传递给 json 参数：

```python
jsons = '{"key1": "value1", "key2": "value2"}'
r = requests.post('https://httpbin.org/post', json=jsons)
print(r.text)
```

执行后终端输出：

```console
{
  "args": {}, 
  "data": "\"{\\\"key1\\\": \\\"value1\\\", \\\"key2\\\": \\\"value2\\\"}\"", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "46", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.28.1", 
    "X-Amzn-Trace-Id": "Root=1-642e79d4-1f0aeb1370ea94cf2c858f9d"
  }, 
  "json": "{\"key1\": \"value1\", \"key2\": \"value2\"}", 
  "origin": "110.191.179.216", 
  "url": "https://httpbin.org/post"
}
```

## 4、响应

其实前面的例子已经有体现一点响应了；

```python
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
```

r 为返回值的对象（Response），通常在项目中我一般用 `rsp` 来表示（后面的 `rsp` 和 r 是一个意思，都是表示返回值的对象）；

rsp 既然是对象，那来看下对象的方法和属性，咱们 Debug 跑一下就很清楚：

![](../../img/spider/rsp.png)

接下来讲几个比较常用的属性和方法；

### 4.1、响应内容

```python
r.text
```

前面例子已经打印过，这里就不打印了；

`text` 的解码是自动的，大多数情况下都能正常解码；

可以通过 `encoding` 来查看或修改编码方式：

```python
print(r.encoding)
r.encoding = 'ISO-8859-1'
```

修改编码方式之后，再使用 `r.text` 就会以新的编码方式解码。

如果你发现返回的内容编码不对，你可以尝试修改不同的编码，这是个经验积累的过程。

### 4.2、二进制响应内容

非文本类请求，一般返回的是二进制内容，此时我们应该使用 `content` 方法：

```python
r.content
```

将二进制文件保存下来，比如请求返回一个 mp3 文件：

```python
with open("my.mp3", "wb") as f：
    f.write(r.content)
```

### 4.3、JSON响应内容

一些 RESTful API 返回通常是 json 内容，我们可以直接使用：

```python
r.json()
```

获取的类型为 Python 的字典类型；

如果响应包含无效JSON，会抛 `requests.exceptions.JSONDecodeError` 异常。

## 5、高阶用法

### 5.1、Session

Session 对象可以在一次会话中可以有效的处理 cookie 持久化的问题；

```python
s = requests.Session()
# 设置一个cookie为123456789
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# 请求一下
r = s.get('https://httpbin.org/cookies')
print(r.text)
```

执行后终端输出：

```console
{
  "cookies": {
    "sessioncookie": "123456789"
  }
}
```

### 5.2、Request

无论是前面讲到的 GET 、 POST 等请求方法：

```python
requests.get()
requests.post()
```

其底层都是通过调用 Request 这个类来实现的：

```python
class Request():
    def __init__(
        self,
        method=None,
        url=None,
        headers=None,
        files=None,
        data=None,
        params=None,
        auth=None,
        cookies=None,
        hooks=None,
        json=None,
    ):
        pass
```

因此我们当然可以直接跨过这一步，不让中间商赚差价，直接用 Request：

```python
frome requests import Request
r = Request("GET", url, headers=headers)
r = Request("POST", url, headers=headers)
```

还没完，记得调用一下 `prepare()` 方法，然后使用 Session 里面的 send 方法：

举例：

```python
from  requests import Session, Request
s = Session()
r = Request("GET", 'https://httpbin.org/get')
prepped = r.prepare()
resp = s.send(prepped)
print(resp.text)
```

执行终端输出：

```console
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "python-urllib3/1.26.13", 
    "X-Amzn-Trace-Id": "Root=1-642e84e2-1328a0210e2252741f20c648"
  }, 
  "origin": "110.191.179.216", 
  "url": "https://httpbin.org/get"
}
```

