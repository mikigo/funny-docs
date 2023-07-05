# selenium—8小时入门版

## 简介

selenium 是专为 web 应用程序编写的一个测试工具。

## 安装

```shell
pip install selenium
```

浏览器驱动，注意一定要和你的浏览器版本匹配；

selenium 驱动  https://npm.taobao.org/mirrors/chromedriver/ 

## 常用控制方法

### 启动浏览器

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http:www.baidu.com")
```

### 浏览器控制

```python
driver.set_window_size(500,500)  #设置窗口为像素500,500大小
driver.maximize_window()  #最大化浏览器
driver.back()     #后退
driver.forward()  #前进
driver.refresh()  #刷新
driver.close()    #关闭当前窗口，但不会切换窗口
driver.quit()     #退出所有窗口  
```

### 8种元素定位方法

#### 1.id

```python
find_element_by_id()
```

#### 2.name

```python
find_element_by_name()
```

#### 3.class_name

```python
find_element_by_class_name()
```

#### 4.tag_name

```python
find_element_by_tag_name()
```

#### 5.link_text

```python
find_element_by_link_text()
```

#### 6.partial_link_text

```python
find_element_by_partial_link_text()
```

#### 7.css_selector

```python
find_element_by_css_selector()
```

（1）.class  比如：.bg 选择类为bg的所有元素
（2）#id  比如：#kw 选择id为kw的元素
（3）element>element 比如：span>input 选择span下的所有input子元素（不含孙）
（4）element element 比如：span input 选择span下的所有input子元素（含孙）
（5）element+element 比如：span+input 选择与span同级的，且紧接着的input元素（只有一个）
（6）[attribute^=value] 比如：a[class^="bg"] 选择类是以bg开头的a元素（$是以什么结尾）
（7）:nth-child 比如：input:nth-child(2) 选择父元素下第2个位置为input的元素（先找位置，再找元素）
（8）:nth-of-type 比如：input:nth-of-type(2) 选择父元素下元素input的第2个（先找元素，再找位置）

#### 8.xpth

```python
find_element_by_xpath()
```

（1）绝对定位

从/html开始，一层一层的往下找。

（2）相对定位，以//开头

- 元素属性定位

  ```py
  driver.find_element_by_xpath（"//input[@id='kw']"），属性值必须加引号。
  ```

- 层级属性结合 

  ```py
  driver.find_element_by_xpath（"//form[@id='form']/span/input"）
  ```

- 使用逻辑运算符

  ```py
  driver.find_element_by_xpath（"//input[@name='wd' and @class='s_ipt']"）
  ```

- 使用contains

  ```py
  driver.find_element_by_xpath（"//input[contains(@class,'bg')]"）
  
  driver.find_element_by_xpath（"//a[contains(text(),'新闻')]"） #查找内容
  
  driver.find_element_by_xpath（"//a[text()='新闻']"）  #查找内容
  ```

### 其他常用

#### 定位一组元素

```python
driver.find_elements_by_css_selector(#form>span>input)
```

返回的是一个列表；

#### 使用By类

```python
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http:www.baidu.com")
driver.find_element(By.ID,'kw')
# 将小写改成大写，比如 name 改成 By.NEME
```

## 简单元素操作

### 1.清除文本

```python
driver.find_element（By.ID,'kw'）.clear()
```

### 2.模拟按键输入

```python
driver.find_element（By.ID,'kw'）.send_keys("苹果")
```

### 3.单击元素

```python
driver.find_element（By.ID,'su'）.click()
```

### 4.提交表单

```python
driver.find_element（By.ID,'su'）.submit()
```

### 5.获取元素信息

```python
① driver.current_url #获取当前url

② driver.find_element_by_link_text("新闻").text  #获取元素的文本内容

③ driver.find_element_by_id("kw").get_attribute("class")  #获取输入框元素的class属性的属性值。
```

### 6.元素再操作
```py
driver.find_element（By.ID,'ul'）.find_element(By.PARTIAL_LINK_TEXT,"新闻").click()
```

## 鼠标事件

### 1.实例

```python
from selenium.wedriver.common.action_chains import ActionChains
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http:www.jd.com")
locator = (By.LINK_TEXT,"家用电器")
locat = driver.find_element(*locator)  
action = ActionChains(driver)    #实例化
action = move_to_element(locat).perform()  #一定要提交
```

### 2.常用的鼠标事件

```python
① context_click(locat)  # 鼠标右键点击
② double_click(locat)  # 左键双击
③ drag_and_drop(source_locat,target_locat)  #鼠标拖动，从source_locat拖动到target_locat
④ move_to_element(locat) #鼠标悬停
⑤ click_and_hold(local) #在元素上按下左键不放
```



## 键盘事件

### 1.实例

```python
from selenium.wedriver.common.keys import Keys  #引入Keys类
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http:www.jd.com")
driver.find_element_by_id("key").send_keys("蒙牛")
driver.find_element_by_id("key").send_keys(Keys.ENTER)
```

### 2.常用的键盘事件

```python
send_keys(Keys.BACK_SPACE) 删除 （与键盘对应）
```

## Select类

### 1.实例

```python
from selenium.wedriver.support.select import Select
...
locat = driver.find_element(By.NAME, 'brand_id')  #找到select元素

select = Select(locat)  #实例化

select.select_by_visible_text("太平鸟")   #选择太平鸟
```

## 内联框架

1.一个网页里面可能会遇到多个frame，不同的frame之间需要切换才能进行操作

2.逐级进入

```python
driver.switch_to.frame("main_frame")  #进入main_frame这一层

driver.switch_to.frame("header_frame")  #再进入header_frame这一层
```

3.跳转到兄弟级

先调到上一级，在进入兄弟级

```python
driver.switch_to.parent_frame("")  #跳到上一级
```

4.跳出所有的frame

```python
driver.switch_to.default_content()
```

## 窗口切换

```python
driver.window_handles 		 	#返回所有窗口的句柄
driver.switch_to.window(handles[1])     #切换窗口
driver.current_window_handle     	#获取当前窗口的句柄
```

## 其他常见控件

### 1.日期控件

能够写的直接写日期，不能写的，去掉readonly属性

```python
js = "document.getElementById('start_date').removeAttribute('readonly')"
driver.execute_script(js)
```

### 2.单选或复选框

找到用click即可；

### 3.表格

```python
tr_list = ele_tboy.find_elements(By.TAG_NAME，'tr') # 获取tr
for tr in tr_list[1:]:
tmp_td_list = tr.find_elements(By.TAGE_NAME,'td') # td元素对象列表
for td in tmp_td_list:  #td就是元素对象
print(td.text)   # 打印表格中的所有内容
# 获取第二行第三列的值
ele_tbody = driver.find_element(By.XPATH,'//*[@id="myTable"]/tbody')  #tbody元素
tr_list = ele_tbody.find_elements(By.TAG_NAME,'tr')   #获取tr
td_list = tr_list[2].find_elements(By.TAG_NAME,'td')   #获取td
print(td_list[2].text)
```



## 警告框处理

在处理警告弹窗之前，仍然需要先点击触发的按钮

### 1.切换到alert页面

```python
driver.find_element(By.ID,'alert').click()
driver.switch_to.alert.text  #获取文本
driver.switch_to.alert.accept()   #点击确定
driver.switch_to.alert.send_keys("警告")   #输入内容
driver.switch_to.alert.dissmiss()      #点击取消
```

### 2.引入Alert类

```python
from selenium.webdriver.common.alert import Alert
...
alert = Alert(driver)
```

## 截图

1.`driver.save_screenshot("screnshot.png")`  #返回一个图片文件

2.浏览器换成PhantomJS，可截整个网页

3.截下一页，可以先将光标移动到下一页，然后截图即可

## 设置等待

### 1.强制等待

```py
from time import sleep
sleep(2)
```



### 2.隐式等待

```py
....
driver = webdriver.Chrome()
driver.implicitly_wait(30)
```

一般在打开浏览器后进行声明，表示：30秒内一旦加载完毕，就执行下一条语句，如果没有，就抛异常。

### 3.显式等待

针对某一个步骤，隐式等待时间不够长，可以专门设置一个显式等待。

```py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
....
#设置等待
wait = WebDriverWait(driver,10,0.5)  #每个0.5秒检查一下，总时间为10秒之内。
wait.until(EC.presence_of_element_located((By.ID,"kw")))  #定位元素
```

## 上传文件

1.input标签

```py
driver.find_element(By.ID,'kw').send_keys('D\\1.jpg') #用send_keys直接给文件路径。
```

2.非input标签（弹窗形式）

用三方工具Auto Windows Info

## 验证码

1.去掉验证码

2.设置万能验证码

3.验证码识别技术

4.操作cookie 

```py
driver.add_cookie(cookie_dict)
```

