# FastAPI—8小时入门版

```shell
# =============================
# Author : mikigo
# Time   : 2023/3/1
# =============================
```

## 一、简介

FastAPI 是一个 Web 服务框架，其主要特点就是"快"。

在 Python Web 服务领域比较知名的就是 Django、Flask，但其性能一直为大家所诟病，以至于很多大型项目会选择基于 Go 语言的 Web 服务框架，比如 beego。而 Django、Flask 较多应用于一些小型网站或者一些个人博客类网站。

应该说，Python 在 Web 后端服务领域是失败的，而 FastAPI 的出现或许有可能为 Python 扳回一局。

FastAPI 之所以能突破 Python 语言本身所带来的性能瓶颈，是因为其主要采用了异步的设计思路，无论是源码还是示例，都有大量协程的写法。

协程，是 Python 唯一能突破线程 GIL（全局解释器锁）、突破进程 CPU 数量限制的高阶编码模式，它使得任务间的切换能够像调用函数一样轻松。协程也是 Python 里面最不好理解的内容之一。

但是没关系，FastAPI 通过非常精良的设计让你不用真正弄懂协程就能轻松使用它。

## 二、安装

系统环境: `deepin`

```console
$ pip3 install fastapi
---> 100%
```

安装 ASGI 服务器，用于启动服务

```console
$ pip3 install "uvicorn[standard]"
---> 100%
```



## 三、简单的例子

定义一个接口，返回简单的 json 响应：

```python
from fastapi import FastAPI

app = FastAPI()
```

这是固定写法，后面的内容就不重复写这两行了；

```python
@app.get("/")
def hello():
    return {"msg": "hello mikigo"}
```

在终端通过命令启动服务：

```console
uvicorn main:app --reload
```

在本机浏览器访问：http://127.0.0.1:8000/；

我个人喜欢在 `py` 文件里面写启动：

```python
import os

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def hello():
    return {"msg": "hello mikigo"}

if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=os.popen("hostname -I").read().split(" ")[0],  # 动态获取本机IP,如果不传默认为127.0.0.1
        port=5000, # 指定一个测试用端口
        reload=True
    )
```

这样直接运行 `py` 脚本：

![demo](../img/fastapi/demo.png)





### OpenAPI 文档

FastAPI 的一个特点就是自带接口文档，只需要在 url 后面加 `docs`：

![](../img/fastapi/docs.png)

你如果不喜欢 Swagger 风格的文档，可以将 `docs` 改成 `redoc`，FastAPI 默认携带两种风格的接口文档。

## 四、Pydantic

FastAPI 是借助 Pydantic 来进行类型声明的，主要有两个用途：

- 对请求体和响应体的参数类型进行声明；
- 在编辑器里面享受代码补全的乐趣；

使用过 Python 的 typing 的同学应该知道【类型标注】，它可以校验参数及返回的类型，使得代码更加严禁，且更具有可读性。

Pydantic 提供了更加强大的类型定义和更加友好的错误提示功能。即使不用 FastAPI，在其他编码中你也可以很有效的使用它。

使用举例：

```python
from datetime import date
from pydantic import BaseModel

def main(user_id: str):
    return user_id

class User(BaseModel):
    id: int
    name: str
    joined: date
```

传递参数进去：

```python
my_user: User = User(id=3, name="mikigo", joined="20230303")

second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}

my_second_user: User = User(**second_user_data)
```

`from pydantic import BaseModel` 里面的 `BaseModel` 记住，通常都是继承这个类来写我们的自定义类型；

将 `Pydantic` 数据类型转换成 JSON：

```python
from fastapi.encoders import jsonable_encoder

json_user = jsonable_encoder(my_user)
```



## 五、参数

FastAPI 是 RESTful 风格的框架，后面例子的接口请求我都使用 Postman 来做，这个只是个人习惯，你可以使用接口文档里面提供的【Try it out】接口调试功能，也可以使用 requests 这类的 HTTP 库进行接口请求，效果是一样的。

### 1、路径参数

#### 1.1 普通路径参数

声明路径参数：

```python
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

路径参数 `item_id` 可以传入到函数中，比如：http://10.8.13.224:5000/items/mikigo 

传递参数为：mikigo，响应如下：

```json
{"item_id":"mikigo"}
```

#### 1.2 有类型的路径参数

声明路径参数：

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

区别是给参数 `item_id` 指定了一个类型 `int`；

如果还是传递参数为：mikigo，http://10.8.13.224:5000/items/mikigo 会报错：

```json
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```

必须要给一个数字才行 http://10.8.13.224:5000/items/520 响应：

```json
{
    "item_id": 520
}
```

这样就完成了路径参数的数据校验；

### 2、查询参数

不属于路径参数的其他函数参数，会被被自动解释为"查询字符串"参数。

```python
@app.get("/items/")
async def read_item(name: str = ""):
    return {"name" : name}
```

查询参数的键值在 URL 的 `？` 之后，并以 `&` 符号分隔，就和我们理解的普通 GET 请求参数传递方式是一样的；

```url
http://10.8.13.224:5000/items/?name=mikigo
```

响应：

```json
{
    "name": "mikigo"
}
```

注意我们在 `read_item(name: str = "")` 给了一个默认值，说明参数是可选的（不传参也可以），如果 直接用`read_item(name: str)` 说明参数是必传的，否则会报错。

### 3、请求体

**请求体**是客户端发送给 API 的数据。**响应体**是 API 发送给客户端的数据。

一般我们说GET方法没有请求体，POST、PUT等方法才有请求体。

举例：

```python
from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None

@app.post("/items/")
async def post_test(item: Item):
    return {"data": item}
```

发一个 POST 请求，参数为：

```json
{
    "name": "mikigo",
    "description": "搞事情"
}
```

返回值：

```json
{
    "data": {
        "name": "mikigo",
        "description": "搞事情"
    }
}
```

### 4、内建参数类型

#### 4.1、Query

Query 一般是用在查询参数里面：

```python
from fastapi import Query

@app.get("/query/")
async def query_test(
        name: Union[str, None] = Query(default=None, max_length=10)
):
    return {"name": name}
```

`Query(default=None, max_length=10)` 里面:

- `default=None` 表示参数可选，默认值为 None，和 `name: str = None` 写法是一个意思；

  如果想要参数必填：`default=...`（没错哈，就是三个点，三个点在 Python 里面是一个省略对象）；

- `max_length=10` 定义了参数的最大长度；

`Query` 支持的参数还有点多，感兴趣可以一个个试：

```python
def Query(
    default: Any = Undefined,
    *,
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    deprecated: Optional[bool] = None,
    include_in_schema: bool = True,
    **extra: Any,
) -> Any:
    pass
```

请求：

```url
http://10.8.13.224:5000/query?name=mikigo
```

响应：

```json
{
    "name": "mikigo"
}
```

#### 4.2、Path

Path 一般是用在路径参数里面：

```python
from fastapi import Path

@app.get("/path/{path_id}")
async def path_test(
        path_id: int = Path(default=...),
        name: Union[str, None] = Query(default=..., max_length=10)
):
    results = {"path_id": path_id}
    if name:
        results.update({"name": name})
    return results
```

可以看的出来 `Path(default=..., max_length=10)` 和 Query 用法几乎一样，不是几乎，就是一样的。

请求：

```url
http://10.8.13.224:5000/path/10?name=mikigo
```

响应：

```json
{
    "path_id": 10,
    "name": "mikigo"
}
```

#### 4.3、Body

Body 一般是用于请求体：

```python
from fastapi import Body

@app.post("/body/")
async def body_test(
        item: Item,
        age: int = Body(default=None, gt=0)
):
    results = {"data": item}
    if age:
        results.update({"age": age})
    return {"results": results}
```

请求：

```url
http://10.8.13.224:5000/body
```

需要构造请求体：

```json
{
  "item": {
    "name": "string",
    "description": "string"
  },
  "age": 2
}
```

响应：

```json
{
    "results": {
        "data": {
            "name": "string",
            "description": "string"
        },
        "age": 2
    }
}
```

#### 4.4、Field

Field 一般用于请求体的字段，对请求体的参数做进一步的约束，它是从 pydantic 导入的：

```python
from pydantic import Field

class FieldItem(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="deepin", max_length=300
    )

@app.post("/field/")
async def field_test(
        item: FieldItem,
        age: int = Body(default=None, gt=0)
):
    results = {"data": item}
    if age:
        results.update({"age": age})
    return {"field": results}
```

请求：

```url
http://10.8.13.224:5000/field
```

构造请求体如下：

```json
{
  "item": {
    "name": "mikigo",
    "description": "1234"
  },
  "age":30
}
```

响应：

```json
{
    "field": {
        "data": {
            "name": "mikigo",
            "description": "1234"
        },
        "age": 30
    }
}
```

#### 4.5、Cookie

先设置 cookie：

```python
@app.post("/cookieset")
async def cookie_set(response: Response):
    response.set_cookie(key="cookie1", value="mikigocookie11111")
    return {"cookie_id": "ok"}
```

请求一下，查看 cookie 设置是否成功:

![](../img/fastapi/set_cookie.png)

然后再定义 Cookie 参数：

```python
from fastapi import Cookie

@app.get("/cookieget")
async def cookie_get(
        ads_id: Union[str, None] = Cookie(default=None)
):
    return {"ads_id": ads_id}
```

 `Cookie` 参数的结构与声明 `Query` 参数和 `Path` 参数时相同

请求一把：

![](../img/fastapi/get_cookie.png)

#### 4.6、Header

`Header` 使用和`Path`, `Query` and `Cookie` 一样;

```python
from fastapi import Header

@app.get("/header")
async def header_test(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}
```

请求：

```url
http://10.8.13.224:5000/header
```

响应：

```json
{
    "User-Agent": "PostmanRuntime/7.31.1"
}
```

`Header` 有个特殊的参数 `convert_underscores: bool = True`；

因为大多数标准的headers用 "连字符" 分隔，因此默认将参数名称的字符从下划线 (`_`) 转换为连字符 (`-`) ；

## 六、响应

### 1、响应限制

`Pydantic` 不仅可以对请求参数进行校验和限制，对响应同样可以；

```python
class Item(BaseModel):
    name: str
    description: Union[str, None] = None

@app.post("/rsp_model/", response_model=Item)
async def response_model_test(item: Item) -> Any:
    return item
```

在装饰器 `@app.post` 里面有个参数 `response_model` 可以声明响应的模型；

`response_model=Item` 表示响应信息也是 `Item` 的类型，API 文档里面也会有响应信息的示例，否则就是空的；

### 2、响应状态码

```python
@app.post("/status", status_code=201)
async def status_code_test(name: str):
    return {"name": name}
```

请求成功，返回状态码为：201;

API 文档里面也会有展示；

fastapi 提供了一个 `status` 模块来表示状态码：

```python
from fastapi import status

@app.post("/status", status_code=status.HTTP_201_CREATED)
async def status_code_test(name: str):
    return {"name": name}
```

`status.HTTP_201_CREATED` 这种方式更容易理解状态码的意思，因此我个人更推荐这种写法。

### 3、返回错误信息

```python
from fastapi import HTTPException
from fastapi import status

names = {"one": "mikigo"}

@app.get("/resp_info/{name_id}")
async def resp_info(name_id: str):
    if name_id not in names:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"item": names[name_id]}
```

发送请求：

![](../img/fastapi/resp_info.png)

## 七、表单及文件

### 1、Form表单

常见的，登录接口会提交 `Form` 表单：

```python
from fastapi import Form

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
```

重启服务，厚礼谢，你会发现报错，提示要安装依赖：`python-multipart`，啥也别问直接装：

```console
pip3 install python-multipart
---> 100%
```

再重启服务之后，通过表单字段发送，注意不能用 JSON 发送；

![](../img/fastapi/form.png)

### 2、上传文件

上传文件功能也依赖：`python-multipart`；

#### 2.1、File

```python
from fastapi import File

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}
```

`File` 是直接继承自 `Form` 的类，把文件当做表单上传，源码：

```python
class File(Form):
    def __init__():
        ...
```

以 `bytes` 形式读取和接收文件内容，这种方式把文件的所有内容都存储在内存里，适用于小型文件。

#### 2.2、UploadFile

```python
from fastapi import UploadFile

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
```

`UploadFile` 与 `bytes` 相比更好一点，即使是大文件也不会占用所有内存，因为它内部有个文件最大限制，超过就会先存入磁盘；

```python
class UploadFile:
    """
    An uploaded file included as part of the request data.
    """

    spool_max_size = 1024 * 1024
    file: typing.BinaryIO
    headers: "Headers"

    def __init__(
        self,
        filename: str,
        file: typing.Optional[typing.BinaryIO] = None,
        content_type: str = "",
        *,
        headers: "typing.Optional[Headers]" = None,
    ) -> None:
        self.filename = filename
        self.content_type = content_type
        if file is None:
            self.file = tempfile.SpooledTemporaryFile(max_size=self.spool_max_size)  # type: ignore[assignment]  # noqa: E501
        else:
            self.file = file
        ... # 省略部分代码
```

`spool_max_size` 就是限制文件的大小；

通过上面源码的构造函数可以看出有 2 个必传参数：

- `filename`：上传文件名字符串（`str`），例如， `mikigo.jpg`；
- `content_type`：内容类型（MIME 类型 / 媒体类型）字符串（`str`），例如，`image/jpeg`；

如果 file 参数不传，默认为 None，那么实际调用的是 `tempfile` 模块子的 `SpooledTemporaryFile` ，这个类会将数据缓存在内存中直到文件大小超过 `max_size`，这时文件内容会被写入磁盘；

`UploadFile` 源码里面有这几个方法：

```python
class UploadFile:
    
    # 省略部分代码

    async def write(self, data: bytes) -> None:
        if self._in_memory:
            self.file.write(data)
        else:
            await run_in_threadpool(self.file.write, data)

    async def read(self, size: int = -1) -> bytes:
        if self._in_memory:
            return self.file.read(size)
        return await run_in_threadpool(self.file.read, size)

    async def seek(self, offset: int) -> None:
        if self._in_memory:
            self.file.seek(offset)
        else:
            await run_in_threadpool(self.file.seek, offset)

    async def close(self) -> None:
        if self._in_memory:
            self.file.close()
        else:
            await run_in_threadpool(self.file.close)
```

这些方法都是异步(`async`)方法：

- `write(data)`：把 `data` （`str` 或 `bytes`）写入文件；
- `read(size)`：按指定数量的字节或字符（`size` (`int`)）读取文件内容；
- `seek(offset)`：移动至文件 `offset（int）`字节处的位置；
  - 例如，`await myfile.seek(0)` 移动到文件开头；
  - 执行 `await myfile.read()` 后，需再次读取已读取内容时，这种方法特别好用；
- `close()`：关闭文件。

使用异步的时候用 `await` ：

```python
contents = await myfile.read()
```

## 八、依赖项

依赖项也叫“依赖注入”，使用 `Depends`：

```python
from fastapi import Depends

async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/dps")
async def depends_test(commons: dict = Depends(common_parameters)):
    return commons
```

`Depends` 需要传入一个可调用对象，一般就给函数对象，也就是依赖函数，注意不是调用函数，没有括号；

依赖函数的参数和查询参数的一样；

## 九、安全性

### 1、OAuth2

功能也依赖：`python-multipart`；

`OAuth2` 主要用于验证用户身份：

```python
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/auth/")
async def auth_test(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

查看 `OpenAPI` 文档你会发现，右上角有个 **Authorize** 按钮，点它：

![](../img/fastapi/auth.png)

弹出授权表单，输入 `username` 与 `password` 及其它可选字段；

这个是 FastAPI 的安全工具；

### 2、获取当前用户

```python
from typing import Union

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
```

先创建一个请求体模型 `User`；

再创建一个 `get_current_user` 依赖项，它的依赖项是 `oauth2_scheme`，这里接受一个 `token` 字符串，在给另外一个函数 `fake_decode_token` 进行解码后，返回 user 对象；

最后，通过 `read_users_me` 依赖项，返回当前用户；

这里实际是一个嵌套依赖的关系。

## 十、中间件

中间件就相当于一个钩子函数，在每个请求被处理之前，以及没饿响应返回之前工作。工作原理类似于 Python 里面的属性拦截器就可以理解。

### 1、创建中间件

使用装饰器 `@app.middleware("http")` ，固定用法，记住就好了；

```python
import time

from fastapi import Request

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)  # 路径操作
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

参数：

- request，FastAPI 的请求对象；
- 一个函数 `call_next` 它将接收 `request` 作为参数；
  - 这个函数将 `request` 传递给相应的 路径操作；
  - 然后它将返回由相应的*路径操作*生成的 `response`；
- 然后你可以在返回 `response` 前进一步修改它；

### 2、跨域资源共享(CORS)

在同一个IP地址中，但使用不同的协议或者端口，就是不同的域；

使用 `CORSMiddleware` ：

```python
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  #  一个允许跨域请求的源列表;
    allow_credentials=True, # 指示跨域请求支持 cookies,默认是 False
    allow_methods=["*"],  # 一个允许跨域请求的 HTTP 方法列表;
    allow_headers=["*"],  # 一个允许跨域请求的 HTTP 请求头列表
)
```

## 十一、SQL数据库

FastAPI 使用数据一般采用 Python 社区最流行的 ORM 库：SQLAlchemy；

如果你会用 Django 的 model，那基本上就很简单了；

### 1、创建数据库工程文件

先创建一个数据库的目录，里面包含这些文件：

```console
.
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```

### 2、安装

安装 SQLAlchemy 非常简单：

```console
pip3 install SQLAlchemy
---> 100%
```

### 3、创建SQLAlchemy部件

SQLAlchemy 支持多种常用的数据类型：

以 sqlite 举例：

```python
# sql_app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 定义数据库的URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  
# 创建 SQLAlchemy 引擎
engine = create_engine(  
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} 
)
# 使用sessionmaker创建一个会话实例
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 创建一个Base类，用这个类继承，来创建每个数据库模型或类
Base = declarative_base()
```

### 4、创建数据库模型

```python
# sql_app/models.py

# 导入一些数据库类型,用于定义一些字段的类型
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# 关系
from sqlalchemy.orm import relationship
# 导入部件Base类用于创建数据库模型
from .database import Base


class User(Base):
    __tablename__ = "users"
	
    # 每一个都代表其相应数据库表中的一列
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
	# 表示该表与其他相关的表中的值
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    # 表示该表与其他相关的表中的值
    owner = relationship("User", back_populates="items")3
```

当访问 `my_user.items` 时，SQLAlchemy 实际上会从 `items` 表中的获取一批记录并在此处填充进去。

注意，数据库模型都是将类型作为参数传给 Column 来定义的，例如：

```python
email = Column(String)
```



### 5、创建 Pydantic 模型

Pydantic 模型和数据库模型的属性一致：

```python
# sql_app/schemas.py

from typing import List, Union
from pydantic import BaseModel
# ========== item的Pydantic模型 ============
# models里面的Item也有title和description属性
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    pass
# 创建用于读取/返回的Pydantic模型/模式
class Item(ItemBase):
    id: int
    owner_id: int
	# 为 Pydantic 提供配置 
    class Config:
        orm_mode = True
        
# ========== user的Pydantic模型 ============
# models里面的User也有email属性
class UserBase(BaseModel):
    email: str
# 在创建时有一个password属性
class UserCreate(UserBase):
    password: str
# 创建用于读取/返回的Pydantic模型/模式
# 读取用户（从 API 返回）时将使用不包括password的User Pydantic模型
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
	# 为 Pydantic 提供配置
    class Config:
        # orm_mode将告诉 Pydantic模型读取数据，即它不是一个dict，而是一个 ORM 模型
        orm_mode = True
```

### 6、CRUD工具

用来与数据库中的数据进行交互，**CRUD**分别为：**增加**、**查询**、**更改**和**删除**，即增删改查；

#### 6.1、读取数据

```python
# sql_app/crud.py

from sqlalchemy.orm import Session
# 导入SQLAlchemy模型和Pydantic模型
from . import models, schemas

def get_user(db: Session, user_id: int):
    """通过ID查询用户"""
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """通过email查询用户"""
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """获取所有用户"""
    return db.query(models.User).offset(skip).limit(limit).all()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    """获取所有项目"""
    return db.query(models.Item).offset(skip).limit(limit).all()
```

#### 6.2、创建数据

```python
# sql_app/crud.py

def create_user(db: Session, user: schemas.UserCreate):
    """创建用户"""
    fake_hashed_password = user.password + "notreallyhashed"
    # 获取数据库模型实例
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    # add方法添加数据
    db.add(db_user)
    # 提交
    db.commit()
    # 刷新
    db.refresh(db_user)
    return db_user

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
```

### 7、主程序

```python
# sql_app/main.py

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 创建依赖项,每个请求有一个独立的数据库会话/连接（SessionLocal）
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# SQLAlchemy模型通讯需要一些等待时间,不能直接使用async和await语句；
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
```

### 8、执行项目

```console
uvicorn sql_app.main:app --reload
```

![](../img/fastapi/sql.png)

以上内容是入门版知识，还有一些进阶的内容或者更加工程化的内容，我想放到 FastAPI 实战里面去写，好啦就先到这里吧，期待进阶内容。