
# OpenCV(Python)基础—9小时入门版

```shell
# =============================================
# Author : mikigo
# =============================================
```

## 一、一句话简介

`OpenCV (Open Source Computer Vision Library) ` 是用 `C++` 语言编写，提供 `Python`、`Java` 等语言 `API`的一个开源计算机视觉库。

## 二、安装

1、`Debian` 系使用 `apt` 安装 `OpencCV`：

```console
sudo apt install python-opencv
```

在 `UOS` 系统上，也可以使用：

```console
sudo apt install python3-opencv
```

支持 `AMD`、`ARM`、`MIPS` 架构安装。

2、安装 `NumPy`：

`NumPy` 是 Python中的一个运算速度非常快的数学库，数组玩到起飞，如果你玩数据科学、机器学习，这是必学库。所有 `OpenCV` 数组结构都转换为 `NumPy` 数组，要想 `OpenCV` 学得好，必须熟悉它，学习 `OpenCV` 基础多少需要了解一点。

```python
sudo apt -y install python3-numpy
```

好多同学安装 `Python` 库都习惯使用 `pip` 安装，实际上 `OpenCV` 也可以，但是目前只支持在 `AMD`，所以考虑到兼容性还是建议使用 `apt` 进行安装，并且官方文档也是建议使用 `apt` 安装。

## 三、入门基础

所有 `OpenCV` 类和函数都放在 `cv` 名称空间中，在 `py` 文件中导入：

```ptyhon
import cv2 as cv
```

后续内容默认都使用了导入。

### 1、图像

#### 1.1、读图像

```python
img = cv.imread()
```

- 参数1：文件路径。(str)
- 参数2：读取图像的方式。
  - cv.IMREAD_COLOR 加载一个彩色图像，忽略 alpha 通道。（默认值）
  - cv.IMREAD_GRAYSCALE 加载图像为灰度模式。
  - cv.IMREAD_UNCHANGED 加载图像，包括 alpha 通道。
  - 还可以简单地分别传递整数1、0或 -1。

#### 1.2、显示图像

```python
cv.show()
```

- 参数1：窗口名称。（str）
- 参数2：图像。（obj）

在窗口中显示图像，窗口自动适合图像大小。

销毁窗口

```python
cv.destroyAllWindows() # 销毁所有窗口
cv.destroyWindow("window_name") # 销毁某个窗口，参数传入窗口名称
```

#### 1.3、写图像

```python
cv.imwrite()
```

- 参数1：文件名。
- 参数2：图像。（obj）

### 2、视频

#### 2.1、从摄像头捕获视频

```python
cap = cv.VideoCapture(0)
```

它的参数可以是设备索引或视频文件的名称。设备索引就是指定哪个摄像头的数字。一般我们连接一个摄像头，所以传0(或-1)。当然可以通过传递1来选择第二个相机，以此类推。

```python
import cv2 as cv
cap = cv.VideoCapture(0)
 # 判断是否打开
if not cap.isOpened(): 
    exit()
while True:  
    # 逐帧捕获
    ret, frame = cap.read()  
    # 判断是否读取到
    if not ret:  
        break
    # 转灰度
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 显示图像
    cv.imshow('frame', gray)
    # 监控键盘信号
    if cv.waitKey(1) == ord('q'):
        break
# 释放
cap.release()
cv.destroyAllWindows()
```

一切都看起来很和谐哈。

需要注意其他的两个判断：

- 有时候摄像头可能没有初始化成功，所以用`cap.isOpened()` 来判断，并退出。
- 可能没有接收到帧，停止循环。

获取视频的一些属性：

```python
cap.get(id)
```

`id` 是一个从0到18的数字，每个数字表示视频的一个属性。每个属性代表什么→（https://docs.opencv.org/4.1.2/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d）

`cap.set()` 属于进阶用法，这里按下不表。

#### 2.2、从文件中播放视频

原理和从摄像头中捕获是一样的，区别在于：

```python
cap = cv.VideoCapture('vtest.avi')
```

参数是文件名称。

#### 2.3、保存视频

```python
out = VideoWriter()
```

- 参数1：文件名
- 参数2：fourcc = cv.VideoWriter_fourcc(*'XVID')
  - FourCC 是一个4字节的代码，用于指定视频编解码器。
  - DIVX, XVID, MJPG, X264, WMV1, WMV2
  - 不同的操作系统有差异 https://www.fourcc.org/codecs.php
- 参数3：帧率
- 参数3：分辨率

```python
import cv2 as cv
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 旋转后写入
    frame = cv.flip(frame, 0)
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# 释放
cap.release()
out.release()
cv.destroyAllWindows()
```

结合前面摄像头捕获视频的代码，看起来很简单～

### 3、绘图

#### 3.1、画线

```python
cv.line()
```

举例：创建一个黑色图像，并从左上角到右下角在上面画一条蓝线

```python
import numpy as np
import cv2 as cv
# 写一个黑色的图像
img = np.zeros((512,512,3), np.uint8)
# 画一根5像素款的蓝线
cv.line(img,(0,0),(511,511),(255,0,0),5)
```

(255,0,0) 代表蓝色，最后一个参数是线的宽度。

#### 3.2、画圆

```python
cv.circle(img,(447,63), 63, (0,0,255), -1)
```

参数：中心坐标和半径

#### 3.3、画矩形

```python
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
```

参数：矩形的左上角和右下角

支持其他图形。。。

## 四、核心功能

### 1、图像的基本操作

#### 1.1、访问和修改像素值

```python
import numpy as np  # 官方建议固定写法
import cv2 as cv
img = cv.imread('messi5.jpg')
px = img[100,100]  
# (100, 100)的像素值[157 166 200]（B、G和R值）
blue = img[100,100,0] 
```

修改

```python
img[100,100] = [255,255,255]
```

直接赋值即可修改，但是直接访问非常缓慢，更好的像素访问和编辑方法:

```python
img.item(10,10,2)  # 访问R值
img.itemset((10,10,2),100)  # 修改R值
```

#### 1.2、访问图像属性

图像属性包括行数、列数和通道数、图像数据类型、像素数等。

```python
img.shape
# (342,548,3)
```

返回一个行、列和通道数的元组。

```python
img.size  # 访问像素总数
```

#### 1.3、特定区域

机器学习中经常需要抠图，比如人脸识别时，一般会先选择人脸区域，搜索其中的眼睛，而不是搜索整个图像，以提供精确度。

```python
ball = img[280:340, 330:390] # 抠一个区域
img[273:333, 100:160] = ball # 复制到另一个区域
```

#### 1.4、图像信道的分裂与合并

```python
b,g,r = cv.split(img)  # 分裂
img = cv.merge((b,g,r))  # 合并
```

或者

```python
b = img[:,:,0]
```

比如将所有红色像素设置为零

```python
img[:,:,2] = 0
```

### 2、图像的算术运算

#### 2.1、图片添加

```python
cv.add()
```

可以添加两个图像

```python
x = np.uint8([250])
y = np.uint8([10])
cv.add(x + y)  # 250+10 = 260 => 255
```

OpenCV 的加法和 Numpy 的加法是有区别的。OpenCV 加法是一个饱和操作，而 Numpy 加法是一个除余操作。

```python
x + y  # 250+10 = 260 % 256 = 4
```

#### 2.2、图像混合

```python
cv.addWeighted()
```

也是图像添加，但不同的权重给予图像，使它给人一种混合或透明的感觉。

- 参数1、2：图像1及其权重。
- 参数3、4：图像2及其权重。
- 参数5：图像混合的α 值，通过改变 α 从0→1，你可以在一张图片到另一张图片之间进行一个很魔幻的转换。

```python
img1 = cv.imread('ml.png')
img2 = cv.imread('opencv-logo.png')
# 第一幅图像的权重为0.7，第二幅图像的权重为0.3
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
```

#### 2.3、按位操作

按位 AND、 OR、 NOT 和 XOR 操作。

可以理解为图像的逻辑运算：

```python
img1 = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo-white.png')
# 把标志放在左上角，所以创建了一个roi
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# 创建一个标志图案，以及它的反面
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY) # 灰度处理
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# 黑掉 ROI 中的 logo 区域
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# 只取标志图像中的标志区域
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# 将 logo 放入 ROI 中，并修改主图像
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
```

## 五、图像处理

### 1、改变色彩空间

OpenCV 目前有150多种颜色空间转换方法。但其中两个最广泛使用的：

#### 1.1、Gray

`cv.COLOR_BGR2GRAY`

顾名思义：BGR → Gray 

这个图像识别中经常使用，可以提供识别速度和准确度。

#### 1.2、HSV

`cv.COLOR_BGR2HSV`

顾名思义：BGR → HSV

HSV 图像可以用它来提取有色物体在 HSV 中，比在 BGR 颜色空间中更容易表示颜色。

```python
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while True:
    # 取出视频的每一帧
    _, frame = cap.read()
    # 从 BGR 到 HSV 颜色空间的转换
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 定义 HSV 中蓝色的范围
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # 得到蓝色
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # 按位-and 蒙版和原始图像
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
```

### 2、几何变换

#### 2.1、缩放

```python
res = cv.resize(InputArray, OutputArray, Size, fx, fy, interpolation)
```

| 参数            | 解释                 |
| :-------------- | -------------------- |
| nputArray src   | 输入图片             |
| OutputArray dst | 输出图片             |
| Size            | 输出图片尺寸         |
| fx, fy          | 沿x轴，y轴的缩放系数 |
| interpolation   | 插入方式             |

`interpolation` 默认情况下，使用的插值方法是  `cv.INTER_LINEAR`，用于所有调整大小。

举例：

```python
import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg')
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
```

#### 2.2、旋转

```python
cv.getRotationMatrix2D()
```

旋转90度：

```python
img = cv.imread('messi5.jpg',0)
rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
```

### 3、图像阈值化

#### 3.1、自适应阈值分割

如果像素值小于阈值，则将其设置为0，否则将其设置为最大值。

```python
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
```

- cv.THRESH_BINARY 
- cv.THRESH_BINARY_INV
- cv.THRESH_TRUNC
- cv.THRESH_TOZERO
- cv.THRESH_TOZERO_INV

如果一个图像在不同的区域有不同的照明条件，全局使用一个阈值一般是不可用的，对同一幅图像的不同区域采用不同的阈值，对不同光照条件下的图像取得了较好的效果。

- cv.ADAPTIVE_THRESH_MEAN_C 阈值是邻近区域的平均值减去常数 c
- cv.ADAPTIVE_THRESH_GAUSSIAN_C  阈值是邻域值减去常数 c 的高斯加权和

```python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('sudoku.png',0)
img = cv.medianBlur(img,5)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
```

### 4、模板匹配

#### 4.1、单目标匹配

模板匹配是一种在较大图像中搜索和查找模板图像位置的方法。

```python
cv.matchTemplate()
```

- 参数1：大图
- 参数2：小图
- 参数3：匹配方法
  - cv.TM_CCOEFF
  - cv.TM_CCOEFF_NORMED
  - cv.TM_CCORR
  - cv.TM_CCORR_NORMED
  - cv.TM_SQDIFF
  - cv.TM_SQDIFF_NORMED

查找最大/最小值

```python
 cv.minMaxLoc()
```

```python
res = cv.matchTemplate(source, template, cv.TM_CCOEFF_NORMED)
cv.minMaxLoc(res)
```

#### 4.2、多目标匹配

`cv.minMaxLoc()`不会给出所有位置。

通过阈值处理多个模板匹配。

```python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv.imread('mario.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('mario_coin.png',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
loc = np.where( res >= 0.8)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('res.png',img_rgb)
```



