# Appium—5小时入门版

## 一、Appium基础

###   adb工具

  1.`android debug brige` 安卓调试桥接器。

  2.`adb` 常用命令

- `adb devices` 查看链接的设备

- `adb pull/push` 在设备与 `pc` 之间拷贝文件

  ```sh
  adb push E:/data/app \data\
  ```

- `adb install/uninstall` 安装/卸载

  ```sh
  adb install E:/app/baidu.apk
  ```

- `adb shell` 进入shell界面（支持Linux命令）

- `adb connect/disconnect` 链接某个设备

  ```sh
  adb connect 127.0.0.1:62001
  ```

###  Package和Activity

- `package` 包，告知工具包名是什么；

- `Activity` 就是一个个的页面，要指定一个主 `Activity`，才能启动；

- 获取 `package` 和 `activity`

  ```sh
  apt dump badging E:/app/baidu.apk
  ```

### 控件布局

1.常见布局（Layout）

（1）`LinearLoyout` 线性布局

（2）`RelativeLayout` 相对布局

（3）`FrameLayout`

2.常见控件

（1）`TextView` 界面上的一段文字，但不允许用户修改

（2）`Button` 按钮

（3）`EditText` 相当于input输入框

（4）`ImageView` 展示图片的控件

（5）ListView 就是一个列表的展示

## 二、Appium脚本

### 认识appium

1.安装 `appium` 之后，点击打开

2.界面有三个选项

（1）`Simple` 默认配置

（2）`Advanced` 高级设置，可自定义配置

（3）`Presets` 修改高级设置中的配置项

### 启动APP的脚本

```py
from appium import webdriver

desired_capabilities = {
    # 平台
    'platformName': 'Android',
    # 设备
    'deviceName': '127.0.0.1:62001',
    # 系统版本
    'platformVersion': '5.1.1',
    # 包名
    'appPackage': 'com.tencent.news',
    # 主activity
    'appActivity': 'com.tencent.news.activity.SplashActivity'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
```

### 常用Capability

- `noReset` 默认每次都按第一次安装的状态启动

  ```shell
  "noReset": True
  ```

- `newCommandTimeout` 等待发送新消息的时间，默认是60秒

  ```sh
  "newCommandTimeout": 70
  ```

- `browserName` 指定浏览器的名称（Chrome、safari）

  ```sh
  "browserName" : 'Chrome'
  ```

## 三、Appium元素定位

### 1.UIAutomatorviewer

（1）打开在 `Android_sdk_windows/tools_xpaths/uiautomatorviewer.bat`

（2）点击左上角按钮，获取 `APP` 快照

（3）鼠标指定快照上的元素，右侧即会显示该元素的信息

（4）保存功能，可将页面快照和元素信息保存下来，方便下次查看。

### 2.原生应用的定位

  定位的方式有以下几种

- 用过 `id`，但 `id` 并不唯一 

  ```py
  driver.find_element_by_id('id').click()
  ```

- 通过class name定位

  ```py
  driver.find_element_by_class_name('class')
  ```

- 通过xpath定位

  ```py
  driver.find_element_by_xpath('xpath')
  ```

​    xpath轴

​    用法：

```xpath
//*[@id='kw']/parent::span
```

| 轴名称             | 结果                                                   |
| ------------------ | ------------------------------------------------------ |
| ancestor           | 选择当前节点的所有先辈（父、祖父等）                   |
| ancestor-or-self   | 选取对当前节点的所有先辈（父、祖父等）以及当前节点本身 |
| attribute          | 选取当前节点的所有属性                                 |
| child              | 选择当前节点的所有属性                                 |
| descendant         | 选取当前节点的所有后代元素（子、孙等）                 |
| descendant-or-self | 选取当前节点的所有后代元素以及当前节点本身             |
| following          | 选取文档当前节点的结束标签之后的所有节点               |
| namespace          | 选取当前节点的所有命名空间节点                         |
| parent             | 选取当前节点的父节点                                   |
| preceding          | 选取文档中当前节点的开始标签之前的所有节点             |
| preceding-sibling  | 选取当前节点之前的所有统计节点                         |

  **（4）层级定位，就是元素再查找**

 ```py
  element = driver.find_element_by_id('id').find_element_by_xpath('path')
 ```

  **（5）引入By类**

```py
  from appium.webdriver.common.mobileby import MobileBy as By
```

### 3.UIAutomator

```py 
 driver.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("resourece-id")')
```

① `new UiSelector().text("text")`

② `new UiSelector().classname("class")`

​    层级关系定位

③当前类往下递归找符合条件的子级控件

    ```py
    new UiSelector().resourceId("resourece-id").childSelector(new UiSelector().resourceId("resourece-id"))
    ```

④从父类往下递归找符合条件的控件

 ```py
 new UiSelector().resourceId("resourece-id").fromParent(new UiSelector().resourceId("resourece-id"))
 ```

（6）获取元素列表

```py
find_elements
```

### 4.混合应用hybrid

（1）Chrome 远程调试

①在浏览器中输入：

      ```url
      chrome://inspect/#devices
      ```

②浏览器上会显示手机上所有APP的web网页的地址

③复制地址在浏览器中访问，即可对元素进行定位

（2）`driver.contexts`

查看 `context` 的情况

```py
driver.switch_to.context('NATIVE_APP') 
```

跳转到原生应用的 `context`

（3）`appium inspector` 定位

在 `appium` 右上角点击放大镜符号，填入 `desired_capabilities` 里面的参数

### 5.web应用

通过 `pc` 端 `chrome` 操作

```py
from selenium import webdriver
from time import sleep

mobile_emulation = {'deviceName': 'Galaxy S5'}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.baidu.com')
sleep(20)
driver.quit()
```

## 四、Appium操作

### 基本操作

1.点击

```py
click（）
```

2.多点触摸

```py
driver.tap(positions, duration=None)
```

3.清除文本

```py
driver.find_element_by_id('id').clear()
```

### 滚动操作

1.元素滚动

按住不放，拖动

```py
driver.scroll(ele_1,ele_2) 
```

传入两个元素

2.元素拖拽

在开始元素长按（1000毫秒）

```py
driver.drag_and_drop(ele_1,ele_2)
```

3.屏幕滑动

```py
driver.swipe(start_x,start_y,end_x,end_y,duration=None)
```

分别传入开始和结束位置的xy轴值

4.快速滑动

```py
driver.flick(start_x,start_y,end_x,end_y)
```

### 输入、键盘和输入法控制

1.模拟输入

```py
send_keys("text")
```

2.发送按键码

```py
driver.press_keycode(66)
```

常用的按键码

```shell
4:返回
66:回车
26:电源键
3:home键
```

3.输入法操作

```py
# 获取当前输入法引擎
active_ime_engine()
# 激活某个输入法
activate_ime_engine(engine)
```

### 获取页面内容

1.获取上下文信息

```py
# 看有没有webview，包含当前会话所有上下文的list
driver.contexts 
# 获取当前上下文
drover/current_context 
```

2.获取当前所在的activity

```py
driver.current_activity
```

```shell
# 任意程序页面，获取当前页面的activity
adb shell dumpsys window | findstr mCurrentFocus 
```

3.获取元素相关内容

① 获取文本值

```py
driver.find_element_by_id('id').text
```

②获取元素属性值

```py
driver.find_element_by_id('id').get_attribute('text')
```

③获取元素大小

```py
driver.find_element_by_id('id').size
```

④获取元素坐标

```py
driver.find_element_by_id('id').location
```

4.检查元素状态

①检查元素是否被选中

```py
driver.find_element_by_id('id').is_selected()
```

②检查元素是否可用

```py
driver.find_element_by_id('id').is_enabled()
```

③获取窗口大小

```py
driver.get_window_size(windowHandle='current')
```

### 等待

1.wait_activity 

等待某个 activity 加载完

```py
# 每隔1秒扫描一下，总共等待10秒
wait_activity('.base.ui.MainActiity',10,1) 
```

2.强制等待

```py
time.sleep(1)
```

3.隐式等待 

只需要声明一次，一般在打开浏览器后进行声明，声明之后对整个driver的生命周期都有效。

```py
driver.implicitly_wait(20)
```

4.显示等待

等待某个元素出现

```py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver,10,0.5)
wait.until(EC.presence_of_element_located(By.ID,'kw'))
```

### 截图

1.截图保存为文件

```py
driver.save_screenshot(C:/filename.png)
```

2.截图并保存为字符串

```py
base64_png = driver.get_screenshot_as_base64()
base64_png_bytes = base64.b64decode(base64_png)

with open('xxx.png','wb') as f:
	f.write(base64_png_bytes)
```

### APP弹窗处理

- `Dialog` 对话框，确定或取消等弹窗
- `Actionbar` 功能框，分享功能从下方弹出的窗口
- `Toast` 提示信息，页面小提示，过几秒钟就自动消失
- `Snackbar` 提示对话框
- `Dialog` 和 `Actionbar` 可以直接用元素定位

### 触屏操作

TouchAction 要使用到这个类里面的方法

```py
from appium.webdriver.common.touch_action import TouchAction
```

1.tap 触摸

```py
tap(element=None, x=None, y=None, count=1)
```

2.press 短按

```py
press(el=None, x=None, y=None)
```

3.long_press 长按

```py
long_press(el=None, x=None, y=None, duration=1000)
```

4.wait 等待

```py
wait(ms=0)
```

5.move_to 移动

```py
move_to(el=None, x=None, y=None)
```

6.release 释放

```py
driver.release()
```

7.perform 提交

```py
driver.perform()
```