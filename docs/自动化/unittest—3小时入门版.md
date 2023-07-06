# unittest—3小时入门版
```shell
# ==================================
# Author : Mikigo
# Time   : 2021/5/23
# ==================================
```

## 简介
由一个或多个自动化测试基础模块、自动化测试管理模块、自动化测试统计模块等组成的工具集合。

## unittest实例

```python
import unittest
class Mytest_A(unittest.TestCase):
    
    @classmethod
    def setUPclass(cls):
    	print("---我是setUPclass----")
        
    def setUp(self):
    	print("我是setup")
        
    def test_a(self):
    	print("-------A----------")
        
    def test_b(self):
    	print("-------B---------")
        
    def tearDown(self):
    	print("我是teardown")
        
    @classmethod
    def tearDownClass(cls):
    	print("-------我是tearDownClass-------")

if __name__ == '__main__':
	unittest.main()
```

### 重要概念
1.Test Case
一个测试用例，就是一个完整的单元，包含了setUp、run、tearDown
2.Test Suite
测试集，用来组装测试用例，通过addTest加载的TestCase的Testsuite中，返回一个TestSuite实例；
3.Test Runner
执行，TestTestRunner类提供的run()方法来执行
4.Test Fixture
环境修复，setUp和tearDown
（三）测试用例组织
获取不同模块下的所有用例
1.TestSuite

# 创建测试集  testSuite
suite = unittest.TestSuite()  
# 添加用例到测试集中
suite.addTest(test_login.TestCrmLogin("test_login"))   
suite.addTest(test_ex.TestEx("test_a"))
#执行测试集
runner = unittest.TextTestRunner()
runner.run(suite)
2.discover方法
#创建测试集
discover = unittest.defaultTestLoader.discover("cases",pattern="*.py")
#执行测试集
with open("xxx.html",'wd') as f:
runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="测试crm登录",description="描述信息")
runner.run(discover)
（四）断言
每个用例当中都需要断言
username_ele = self.driver.find_element(By.NAME."admin")
self.assertEqual("username",username_ele,"message") > (预期结果，实际结果)
（五）参数化
1.安装ddt（数据驱动测试）：pip install ddt
2.实例
① 单个参数
import ddt
@ddt.ddt
class TestCrmLogin(unittest.TestCase):
@ddt.data("admin","a")
def test_ddt(self,username)
print(username)
备注：@ddt.data("admin","a")，括号里面有几个元素就会跑几遍
② 多个参数
import ddt
@ddt.ddt
class TestCrmLogin(unittest.TestCase):
@ddt.data(("a","admin123")，("admin","admin"))
@ddt.unpack
def test_ddt(self,username,password)
print(username,password)
3.excel文件读取
import xlrd
def get_excel_user_data(file):
    data = xlrd.open_workbook(file)
    table = data.sheet_by_name("login")
    e_list = []
    for n_row in range(1, table.nrows):
        user = tuple(table.row_values(n_row))
        users = e_list.append(user)
    return users
4.获取路径和时间
import os
import time
times = time.strftime("%Y%m%d%H%M%S")
report_file = "crm_%s_result.html" % times
# tmp_base_path = os.path.abspath(__file__)
# tmp_base_path = os.path.dirname(tmp_base_path)
# base_path_list = tmp_base_path.split('\\')[0:-1]
# base_path = "\\".join(base_path_list)
base_path = "\\".join(os.path.dirname(os.path.abspath(__file__)).split('\\')[0:-1])
report_path = os.path.join(base_path, "report")
（六）Page Object
1.Page Object是一种自动化测试思想，其理念是将页面的交互细节封装起来，使用例更关注业务而非界面细节，从而提高测试案例的可读性，提高项目的可维护性。
2.规范项目文件夹
① driver 驱动文件，用户存放浏览器驱动文件等
② model 函数文件夹，启动浏览器等
③ page 页面文件夹，所有的基类（定位器、找元素）
④ testcase 测试用例，用例的基类
⑤ 存放测试报告，截图等测试结果文件
3.一个页面一个类，一个元素一个方法。