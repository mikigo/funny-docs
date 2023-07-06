# unittest—3小时入门版
```shell
# ==================================
# Author : Mikigo
# Time   : 2020/5/23
# ==================================
```

## 简介
由一个或多个自动化测试基础模块、自动化测试管理模块、自动化测试统计模块等组成的工具集合。

## unittest实例

```python
import unittest

class MytestA(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
    	print("--- 我是setUpClass ----")
        
    def setUp(self):
    	print("我是setup")
        
    def test_a(self):
    	print("------- A ----------")
        
    def test_b(self):
    	print("------- B ---------")
        
    def tearDown(self):
    	print("我是teardown")
        
    @classmethod
    def tearDownClass(cls):
    	print("-------我是tearDownClass-------")

if __name__ == '__main__':
	unittest.main()
```

## 重要概念
### Test Case

一个测试用例，就是一个完整的单元，包含了 `setUp`、`run`、`tearDown`；

### Test Suite

测试集，用来组装测试用例，通过 `addTest` 加载的 `TestCase` 的 `Testsuite` 中，返回一个 `TestSuite` 实例；

### Test Runner

执行，`TestTestRunner` 类提供的run()方法来执行；

### Test Fixture

环境修复，`setUp` 和 `tearDown`；

## 测试用例组织
获取不同模块下的所有用例；

### `TestSuite`

创建测试集  `testSuite`：

```py
suite = unittest.TestSuite()  
```

添加用例到测试集中：

```py
suite.addTest(test_login.TestCrmLogin("test_login"))   
suite.addTest(test_ex.TestEx("test_a"))
```

执行测试集：

```py
runner = unittest.TextTestRunner()
runner.run(suite)
```

### `discover` 方法

```py
#创建测试集
discover = unittest.defaultTestLoader.discover("cases",pattern="*.py")
#执行测试集并生成测试报告
with open("xxx.html",'wd') as f:
    # 使用三方库HTMLTestRunner执行
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="测试登录",description="描述信息")
    runner.run(discover)
```

## 断言
每个用例当中都需要断言

```py
import unittest

class MyTest(unittest.TestCase):
    
    def test_01(self):
        ...
        username_ele = self.driver.find_element(By.NAME."admin")
        self.assertEqual("username",username_ele,"message")
```

## 参数化
1.安装 `ddt`（数据驱动测试）：

```shell
pip install ddt
```

2.使用方法

① 单个参数

```py
import ddt

@ddt.ddt
class TestCrmLogin(unittest.TestCase):
    
    @ddt.data("admin","a")
    def test_ddt(self,username)
        print(username)
```

备注：@ddt.data("admin","a")，括号里面有几个元素就会跑几遍

② 多个参数

```py
import ddt

@ddt.ddt
class TestCrmLogin(unittest.TestCase):
    
    @ddt.data(("a","admin123")，("admin","admin"))
    @ddt.unpack
    def test_ddt(self,username,password)
    	print(username,password)
```

## Page Object

- Page Object是一种自动化测试思想，其理念是将页面的交互细节封装起来，使用例更关注业务而非界面细节，从而提高测试案例的可读性，提高项目的可维护性。
- 规范项目文件夹：
  ① `driver` 驱动文件，用户存放浏览器驱动文件等；
  ② `model` 函数文件夹，启动浏览器等；
  ③ `page` 页面文件夹，所有的基类（定位器、找元素）；
  ④ `testcase` 测试用例，用例的基类；
  ⑤ 存放测试报告，截图等测试结果文件；
- 一个页面一个类，一个元素一个方法。