# locust—2小时入门版

```shell
# ==================================
# Author : Mikigo
# Time   : 2023/3/24
# ==================================
```

## 一、简介

性能测试通常指的是 `API` 性能测试，使用 `JMeter` 做的同学会多一点，因为它开源免费，提供了一些插件，只需要在图形化的界面录入一些数据就能很方便的进行接口测试、性能测试，相比于商用软件 `LoadRunner`更适合普通玩家，所以 `JMeter` 群众基础更好。

locust 是近几年才流行起来的，主要是因为需要编码，所以好多同学有点抵触，但其功能完全不输 `JMeter` ；

## 二、安装

```shell
pip3 install locust
```

检查是否安装成功：

```shell
locust -V
```

## 三、用例模板

```python
# template.py

import random
from locust import TaskSequence, HttpLocust, task, seq_task, between


# 定义一个任务类，这个类名称自己随便定义，类继承 TaskSequence 或 TaskSet类
# 当类里面的任务请求有先后顺序时，继承TaskSequence类， 没有先后顺序，可以使用继承TaskSet类
class MyTaskCase(TaskSequence):
    
    # 初始化方法，相当于 setup
    def on_start(self):
        pass

    # @task 
    # python中的装饰器，告诉下面的方法是一个任务，任务就可以是一个接口请求，
    # 这个装饰器和下面的方法被复制多次，改动一下，就能写出多个接口
    # 装饰器后面带上(数字)代表在所有任务中，执行比例
    # 要用这个装饰器，需要头部引入 从locust中，引入 task
    @task
    # 装饰器，定义有执行顺序的任务，扩展中的数字，从小到大，代表先后执行顺序
    @seq_task(1)  
    # 一个方法， 方法名称可以自己改
    def regist_(self): 
        # 接口请求的URL地址
        url = '/erp/regist'
        # 定义请求头为类变量，这样其他任务也可以调用该变量
        self.headers = {"Content-Type": "application/json"} 
        self.user = "locust_" + str(random.randint(10000, 100000))
        self.pwd = '1234567890'
        # post请求的 请求体
        data = {"name": self.user, "pwd": self.pwd}
        # 使用self.client发起请求，请求的方法根据接口实际选,
        # catch_response 值为True 允许为失败 ， name 设置任务标签名称   -----可选参数
        rsp = self.client.post(url, json=data, headers=self.headers, catch_response=True, name='api_regist')
        if rsp.status_code == 200:
            rsp.success()
        else:
            rsp.failure('regist_ 接口失败！')

    @task 
    # 顺序任务装饰器，说明下面的任务，第二个执行
    @seq_task(2)  
    def login_(self):
        url = '/erp/loginIn' 
        data = {"name": self.user, "pwd": self.pwd}
        # 使用self.client发起请求，请求的方法 选择post
        rsp = self.client.post(url, json=data, headers=self.headers, catch_response=True) 
        # 提取响应json 中的信息，定义为 类变量
        self.token = rsp.json()['token']    
        if rsp.status_code == 200 and rsp.json()['code'] == "200":
            rsp.success()
        else:
            rsp.failure('login_ 接口失败！')

    @task
    @seq_task(3) 
    def getuser_(self):
        url = '/erp/user'
        # 引用上一个任务的 类变量值,实现参数关联
        headers = {"Token": self.token}  
        # 使用self.client发起请求，请求的方法 选择 get
        rsp = self.client.get(url, headers=headers, catch_response=True)  
        if rsp.status_code == 200:
            rsp.success()
        else:
            rsp.failure('getuser_ 接口失败！')

    # 结束方法， 相当于teardown
    def on_stop(self):
        pass


# 定义一个运行类 继承HttpLocust类
class UserRun(HttpLocust):
    # 定义固定的 task_set  指定前面的任务类名称
    task_set = MyTaskCase
    # 设置运行过程中间隔时间 需要从 locust 中 引入 between
    wait_time = between(0.1, 3)  
```

执行时在终端输入：

```shell
locust -f template.py 
```

## 四、简单测试

### 1、mock接口

咱们先使用 `FastAPI` 简单 `Mock` 一个接口：

```python
# mock.py
import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_item(name: str = ""):
    return {"name": name}


if __name__ == '__main__':
    uvicorn.run(
        app="mock:app",
        host=os.popen("hostname -I").read().split(" ")[0], # 自动获取本机IP
        port=5000,
        reload=True
    )
```

### 2、测试用例

```python
# demo_1.py

from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/items?name=mikigo")
```

## 五、在线运行

```shell
locust -f demo_1.py 
```

终端会提示一个链接，使劲戳他：

```shell
$ locust -f demo_1.py 
[2023-07-13 17:55:51,182] uos-PC/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 
```

![](../img/locust/1.jpg)

