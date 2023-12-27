# HttpRunner—2小时入门版

```shell
# ==================================
# Author : mikigo
# ==================================
```

## 一、简介

接口测试很多同学用 `Postman`、`Jmeter` 来做，用起来也挺简单的，但是接口用例多了之后就发现不好管理维护，要落地到公司级 CI 项目就有点难搞了；

稍微有点技术能力的同学更愿意直接用 `requests` 来做接口自动化，但是大多用 `requests` 来做的接口自动化项目，在工程化方面都做得不太好，与其说是接口自动化项目，不如说是接口脚本的集中存放，没有体系化的框架结构设计，因此在大型 CI 项目中落地也显得不太够用，维护人员除了忙于接口脚本的维护，还要投入大量时间做新功能和修复代码中的 Bug。

想要轻松快速的落地接口自动化，又不想自己去折腾，我个人还是推荐 `HttpRunner`，只需要写写配置文件就把活干完了；

## 二、安装

系统环境：`deepin` / `UOS`

```console
sudo bash -c "$(curl -ksSL https://httprunner.com/script/install.sh)"
```

注意，使用 `sudo` 安装，不然命令行工具无法写入系统环境变量。

装完之后会有一些版本、命令行参数的输出，说明安装成功。

## 三、创建项目

```shell
hrp startproject funny-api-autotest
```

这里会使用 `venv` 创建一个虚拟，有可能报错需要安装 `python3-venv`；

不要慌，我们来修复一下环境：

```shell
# 安装依赖
sudo apt install python3-pip
# 安装venv
sudo apt install python3-venv
# 把之前创建失败的虚拟环境删掉
cd ~/.hrp/
rm -rf venv
# 重新创建一个
python3 -m venv venv
# 激活虚拟环境
source ~/.hrp/venv/bin/activate
# 把pip更新一下
pip install --upgrade pip setuptools wheel
# 安装依赖funppy
pip install funppy
```

如果不出意外，环境就安装好了；

## 四、目录结构

```shell
.
├── debugtalk.py # 定义一些函数并返回一些值，函数名和参数可以传入到yml文件参数里面；
├── .env # 定义全局的环境变量
├── .gitignore
├── har # 导出的har文件
├── proj.json # 工程信息
├── README.md
├── results # 测试报告
└── testcases # 测试用例
```

 **`testcases`** 

这里面用例是 `yaml` 或 `json` 文件，用 `yaml ` 文件写接口自动化的用例也是常规操作，因为接口几乎都是以字典（或 `json`）的形式提供参数，而 `yaml` 文件读出来刚好就是，所以大家就喜欢用这种格式。

前面我说这个框架简单就是因为把接口的信息就直接在 `yaml` 文件里面一配置，活就干完了，根本都不需要写代码；

对新手来说简直了，下面介绍一下 `yaml` 文件的字段：

```yaml
config:
    name: "request methods testcase with functions"
    variables:
        foo1: config_bar1
        foo2: config_bar2
        expect_foo1: config_bar1
        expect_foo2: config_bar2
    base_url: "https://postman-echo.com"
    verify: False
    export: ["foo3"]

teststeps:
-
    name: get with params
    variables:
        foo1: bar11
        foo2: bar21
        sum_v: "${sum_two(1, 2)}"
    request:
        method: GET
        url: /get
        params:
            foo1: $foo1
            foo2: $foo2
            sum_v: $sum_v
        headers:
            User-Agent: HttpRunner/${get_httprunner_version()}
    extract:
        foo3: "body.args.foo2"
    validate:
        - eq: ["status_code", 200]
        - eq: ["body.args.foo1", "bar11"]
        - eq: ["body.args.sum_v", "3"]
        - eq: ["body.args.foo2", "bar21"]
-
    name: post form data
    variables:
        foo2: bar23
    request:
        method: POST
        url: /post
        headers:
            User-Agent: HttpRunner/${get_httprunner_version()}
            Content-Type: "application/x-www-form-urlencoded"
        data: "foo1=$foo1&foo2=$foo2&foo3=$foo3"
    validate:
        - eq: ["status_code", 200]
        - eq: ["body.form.foo1", "$expect_foo1"]
        - eq: ["body.form.foo2", "bar23"]
        - eq: ["body.form.foo3", "bar21"]
```

- config：测试用例的公共配置部分，包括用例名称、base_url、参数化数据源、是否开启 SSL 校验等，举例：

  ```yaml
  config:
    name: "demo with complex mechanisms"
    verify: False
    base_url: "https://postman-echo.com"
    headers:
      X-Request-Timestamp: "165460624942"
    parameters:
      user_agent: [ "iOS/10.1", "iOS/10.2" ]
      username-password: ${parameterize($file)}
    parameters_setting:
      strategies:
        user_agent:
          name: "user-identity"
          pick_order: "sequential"
        username-password:
          name: "user-info"
          pick_order: "random"
      limit: 6
    think_time:
      strategy: random_percentage
      setting:
        max_percentage: 1.5
        min_percentage: 1
      limit: 4
    variables:
      app_version: v1
      user_agent: iOS/10.3
      file: examples/hrp/account.csv
    websocket:
      reconnection_times: 5
      reconnection_interval: 2000
    export: ["app_version"]
    weight: 10
  ```

- teststeps：有序步骤的集合；

  | 测试步骤类型 | 含义                              |
  | ------------ | --------------------------------- |
  | request      | 用于发起 HTTP 请求的步骤类型      |
  | api          | 用于引用 API 的步骤类型           |
  | testcase     | 用于引用其他测试用例的步骤类型    |
  | transaction  | 用于定义一个事务                  |
  | rendezvous   | 集合点                            |
  | think_time   | 思考时间                          |
  | websocket    | 用于发起 WebSocket 请求的步骤类型 |

  除了基本的测试步骤之外，部分测试步骤还可以进行增强；

  | 增强操作类型   | 含义     | 适用的测试步骤        |
  | -------------- | -------- | --------------------- |
  | variables      | 局部变量 | 通用                  |
  | setup_hooks    | 前置函数 | request/api/websocket |
  | teardown_hooks | 后置函数 | request/api/websocket |
  | extract        | 参数提取 | request/api/websocket |
  | validate       | 结果校验 | request/api/websocket |
  | export         | 导出变量 | testcase              |

  举例：

  ```yaml
  teststeps:
    -
      name: get with params
      variables:
        foo1: ${ENV(USERNAME)}
        foo2: bar21
        sum_v: "${sum_two_int(1, 2)}"
      request:
        method: GET
        url: $base_url/get
        params:
          foo1: $foo1
          foo2: $foo2
          sum_v: $sum_v
      extract:
        foo3: "body.args.foo2"
      validate:
        - eq: ["status_code", 200]
        - eq: ["body.args.foo1", "debugtalk"]
        - eq: ["body.args.sum_v", "3"]
        - eq: ["body.args.foo2", "bar21"]
    -
      name: post form data
      variables:
        foo2: bar23
      request:
        method: POST
        url: $base_url/post
        headers:
          Content-Type: "application/x-www-form-urlencoded"
        body: "foo1=$foo1&foo2=$foo2&foo3=$foo3"
      validate:
        - eq: ["status_code", 200]
        - eq: ["body.form.foo1", "$expect_foo1"]
        - eq: ["body.form.foo2", "bar23"]
        - eq: ["body.form.foo3", "bar21"]
  ```

**特殊值的规则：**

- 变量引用：约定通过 `${}` 或 `$` 的形式来引用变量，例如 `$foo1` 或 `${foo1}`

- 函数调用：约定通过 `${}` 的形式来调用插件函数，例如 `${sum_two(1, 2)}` ；

  有同学要问了，yaml 文件里面写 `${sum_two(1, 2)}`，从哪里来的；

  其实，`sum_two` 在`debugtalk.py` 里面定义;

  ```python
  # debugtalk.py
  
  import funppy
  
  def sum_two_int(a: int, b: int) -> int:
      return a + b
  
  if __name__ == '__main__':
      funppy.register("sum_two", sum_two_int)
      funppy.serve()
  ```

## 五、执行用例

```shell
hrp run testcases/demo_requests.yml --gen-html-report
```

执行完成之后，在 `result` 目录下生成 `html` 测试报告。

## 六、实例

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

看看接口文档，非常简单的一个接口

![](../img/httprunner/1.png)

好，那咱们回到httprunner里面来写用例了；

### 2、写接口用例

用例也非常简单：

```yaml
# testcases/demo_1.yml

config:
    name: "demo_1"
    variables:
        name: mikigo
    verify: False

teststeps:
-
    name: get with params
    request:
        method: GET
        url: http://10.8.7.199:5000/items/  # ip写你的机器的ip
        params:
            name: mikigo
    validate:
        - eq: ["status_code", 200]
        - eq: ["body.name", "mikigo"]

```

### 3、执行用例

使用hrp命令执行

```shell
hrp run testcases/demo_1.yml --gen-html-report
```

run 是使用 go 驱动执行；

如果你习惯使用 pytest：

```shell
hrp pytest testcases/demo_1.yml
```

后面你要生成什么报告，加什么参数就完全按照 `pytest` 的规范来就好，不过 `pytest` 那一套咱们已经熟得不能再熟了，没啥意思，就用 go 驱动吧。

跑完之后在 `results` 目录下生成一个 `html` 文件，打开它：

![](../img/httprunner/2.png)

## 七、debugtalk.py底层实现原理

前面讲到可以在 `debugtalk.py` （下面就用“它”指代）里面定义一些变量或函数，然后在用例里面通过 `$var` 、`${func()}` 的方式调用；

这章咱们就讲讲，为啥在 `debugtalk.py` 里面定义的代码，能在 `yaml` 文件里面写字符串的方式调用；

### 1、获取路径

在 `loader.py` 里面：

```python
# loader.py
def locate_project_root_directory(test_path: Text) -> Tuple[Text, Text]:
    """locate debugtalk.py path as project root directory

    Args:
        test_path: specified testfile path

    Returns:
        (str, str): debugtalk.py path, project_root_directory

    """
    ...
    return debugtalk_path, project_root_directory
```

很明显返回了两个路径：`ebugtalk_path`, `project_root_directory`

### 2、原始数据

```python
# loader
def load_project_meta(test_path: Text, reload: bool = False) -> ProjectMeta:
    """load testcases, .env, debugtalk.py functions.
        testcases folder is relative to project_root_directory
        by default, project_meta will be loaded only once, unless set reload to true.

    Args:
        test_path (str): test file/folder path, locate project RootDir from this path.
        reload: reload project meta if set true, default to false

    Returns:
        project loaded api/testcases definitions,
            environments and debugtalk.py functions.

    """
    ...
    return project_meta
```

返回的 `project_meta` 是 `pydantic` 的模型对象，你可以理解成就是一个字典；

在这个函数里面主要逻辑是通过一个函数获取它里面的函数对象：

```python
# loader
def load_module_functions(module) -> Dict[Text, Callable]:
    """load python module functions.

    Args:
        module: python module

    Returns:
        dict: functions mapping for specified python module

            {
                "func1_name": func1,
                "func2_name": func2
            }

    """
    module_functions = {}
    for name, item in vars(module).items():
        if isinstance(item, types.FunctionType):
            module_functions[name] = item
    return module_functions
```

这里面主要用到了 `vars` 函数来获取，感兴趣的同学可以去查一下这个用法；

到这里也就是说获取到了它里面的 `函数名` 及 `函数对象` ，有了函数对象在合适的位置调用就行了；

咱们接着往后看；

### 3、参数解构

在 `parser.py` 中进行参数结构：

```python
# parser.py
def parse_parameters(
    parameters: Dict,
) -> List[Dict]:
    """parse parameters and generate cartesian product.

    Args:
        parameters (Dict) parameters: parameter name and value mapping
            parameter value may be in three types:
                (1) data list, e.g. ["iOS/10.1", "iOS/10.2", "iOS/10.3"]
                (2) call built-in parameterize function, "${parameterize(account.csv)}"
                (3) call custom function in debugtalk.py, "${gen_app_version()}"

    Returns:
        list: cartesian product list
    """
    ...
    return utils.gen_cartesian_product(*parsed_parameters_list)
```

经过一系列的数据处理，把参数列表返回出来

### 4、函数调用

```python
# parser.py
def parse_string(
    raw_string: Text,
    variables_mapping: VariablesMapping,
    functions_mapping: FunctionsMapping,
) -> Any:
    """parse string content with variables and functions mapping.

    Args:
        raw_string: raw string content to be parsed.
        variables_mapping: variables mapping.
        functions_mapping: functions mapping.

    Returns:
        str: parsed string content.

    Examples:
        >>> raw_string = "abc${add_one($num)}def"
        >>> variables_mapping = {"num": 3}
        >>> functions_mapping = {"add_one": lambda x: x + 1}
        >>> parse_string(raw_string, variables_mapping, functions_mapping)
            "abc4def"

    """
    
```

在这个函数里面主要代码：

```python
# parser.py
def parse_string(
    raw_string: Text,
    variables_mapping: VariablesMapping,
    functions_mapping: FunctionsMapping,
) -> Any:
	...
    while match_start_position < len(raw_string):
        ...
        if func_match:
            func_name = func_match.group(1)
            func = get_mapping_function(func_name, functions_mapping)

            func_params_str = func_match.group(2)
            function_meta = parse_function_params(func_params_str)
            args = function_meta["args"]
            kwargs = function_meta["kwargs"]
            parsed_args = parse_data(args, variables_mapping, functions_mapping)
            parsed_kwargs = parse_data(kwargs, variables_mapping, functions_mapping)

            try:
                func_eval_value = func(*parsed_args, **parsed_kwargs)
            except Exception as ex:
				...
            ...
    return parsed_string
```

`func` 为函数对象，通过 `parse_data` 函数获取到参数 `parsed_args` 和 `parsed_kwargs`，通过 `func(*parsed_args, **parsed_kwargs)` 调用函数并获取到值；

最后经过一顿组装返回最终的字符串；

### 5、变量获取

变量获取相对简单，不想函数调用，要考虑函数对象及参数；

```python
# parser.py
def parse_variables_mapping(
    variables_mapping: VariablesMapping, functions_mapping: FunctionsMapping = None
) -> VariablesMapping:
    ...
    while len(parsed_variables) != len(variables_mapping):
        ...
            try:
                parsed_value = parse_data(
                    var_value, parsed_variables, functions_mapping
                )
            except exceptions.VariableNotFound:
                continue
            ...
    return parsed_variables
```

也是通过 `parse_data` 函数来获取；

### 6、驱动入口

```python
# runner.py
class SessionRunner(object):
	
    ...

    def __parse_config(self, param: Dict = None) -> None:
        # parse config variables
        self.__config.variables.update(self.__session_variables)
        if param:
            self.__config.variables.update(param)
        self.__config.variables = self.parser.parse_variables(self.__config.variables)

        # parse config name
        self.__config.name = self.parser.parse_data(
            self.__config.name, self.__config.variables
        )

        # parse config base url
        self.__config.base_url = self.parser.parse_data(
            self.__config.base_url, self.__config.variables
        )
        
    ...

    def test_start(self, param: Dict = None) -> "SessionRunner":
        """main entrance, discovered by pytest"""
        ...
        self.__parse_config(param)
        ...
```

在入口文件 `runner.py` 里面把上面所有的逻辑串起来；

在 `test_start` 里面调用私有方法 `__parse_config`，在 `__parse_config` 里面挨个处理前面的逻辑；

在 `step` 里面通过：

```python
runner = HttpRunner().test_start()
```

进行驱动执行；

