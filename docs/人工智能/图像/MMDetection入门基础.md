# MMDetection 入门基础

```shell
# =============================================
# Author : mikigo
# =============================================
```

MMDetection 是商汤科技开源的一个深度学习框架，国内目标检测领域的翘楚；

相比于 Facebook 开源的 Detectron 框架，作者声称 MMDetection 有三点优势：performance 稍高、训练速度稍快、所需显存稍小。

低调哈，基操，皆坐，勿6，又被他装到了～

Github地址：https://github.com/open-mmlab/mmdetection

## 一、虚拟环境安装

```shell
cd ~
wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

一路回车

第一次提示输入  yes/no ：输入  `yes`

继续一路回车

第二次提示：输入  `no`

```shell
cd ~/miniconda3/bin
sudo chmod 777 activate
```

激活conda环境

```shell
. ./activate
```

添加公司内网源

```shell
conda config --add channels bioconda
conda config --add channels conda-forge
```

如果是外网添加外网源

```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
```

如果要删除源

```shell
conda config --remove-key channels
```

## 二、安装依赖

### 1、创建虚拟环境

```shell
conda remove --name mmlab --all # 移除所有虚拟环境
```
```shell
conda create -n mmlab python=3.7
```

```shell
conda activate mmlab
```


### 2、安装 Pytorch 

在mmlab虚拟环境中执行

```shell
pip install torch==1.7.0+cu101 torchvision==0.8.1+cu101 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```
### 3、安装 MMCV

在mmlab虚拟环境中执行

```shell
pip install mmcv-full==1.3.3 -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.7.0/index.html -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

### 4、安装显卡驱动

显卡为 `GTX1660`，驱动版本为 430，驱动下载地址：https://www.nvidia.cn/Download/Find.aspx?lang=cn

```shell
CTRL+ALT+F2 进入tty
```

禁用 nouveau 驱动

```shell
sudo vim /etc/modprobe.d/blacklist-nouveau.conf
```

填入：

```shell
blacklist nouveau 
options nouveau modeset=0
```

刷新配置文件

```shell
sudo update-initramfs -u 
```

reboot 重启后再进入 tty

关闭图像界面，输入命令关闭图像界面

```shell
sudo service lightdm stop
```

安装驱动

```shell
sudo chmod a+x NVIDIA-Linux-x86_64-430.run
sudo ./NVIDIA-Linux-x86_64-430.run
```

reboot重启，nvidia-smi查看安装状态。注意看下cuda版本，10.1，driver版。

## 三、数据标注

标注之前需要先转换图片大小，并且以数字命名，每组命名递增

### 1、转换大小并重命名

rename_pic.py

```python
import os
import sys
import cv2
import time
import getpass
username = getpass.getuser()

source_path = f"/home/{username}/Desktop/right_menu" # 图片路径

source_dest = os.path.join('/'.join(source_path.split("/")[:-1]), 'tmp')
if not os.path.exists(source_dest):
    os.mkdir(source_dest)

start_name = sys.argv[1]

file_name_list = list()
for file in os.listdir(source_path):
    if file.endswith('.png'):
        file_name_list.append(file)
start_name = int(start_name)
for file in file_name_list:
    os.rename(os.path.join(source_path,file), os.path.join(source_path, f"{str(start_name)}.png"))
    start_name += 1

time.sleep(1)

for file in os.listdir(source_path):
    image = os.path.join(source_path, str(file))
    src = cv2.imread(image)
    result = cv2.resize(src, (960, 540))
    resizeImage = os.path.join(source_dest, str(file))
    print(resizeImage)
    cv2.imwrite(str(resizeImage), result)
cv2.waitKey(0)
cv2.destroyAllWindows()

time.sleep(1)

os.system(f'rm -rf {source_path}/*')
os.system(f'mv {source_dest}/* {source_path}')
os.system(f'rm -rf {source_dest}')

print("下一个序号：", start_name)
```

根据终端输出的下一个序号的提示，执行 Python 文件的时候传参。

```shell
python rename_pic.py 249
```

### 2、工具标注

使用工具 labelImg 标注

```shell
sudo pip3 install PyQt5==5.13
sudo pip3 install labelImg
```

终端直接输入 labelImg，回车

标注模式选择：`PascalVOC`

## 四、拉取 MMDetection 代码

```shell
cd ~/Documents
git clone https://github.com/open-mmlab/mmdetection.git
# 不能直接拉取主分支，建议使用2.12版本，不同的版本对应的mmcv版本是不同的
```

## 五、拉取 voc2coco 代码

```shell
cd ~/Documents
git clone https://github.com/Tony607/voc2coco.git
```

## 六、转换 coco 数据集

将所有的图片和xml文件放入train2017，从中挑选几组放入val2017（测试集）

```shell
cd mmdetection/data/coco
python voc2coco.py train2017 annotations/instances_train2017.json
python voc2coco.py val2017 annotations/instances_val2017.json
```

生成json文件

## 七、修改配置

### 1、读取模型名称

```python
import json

module_name = []
with open('./instances_train2017.json', "r+") as f:
    json_file = f.read()
json_dict = json.loads(json_file)
module_list = json_dict.get('categories')
for module_info in module_list:
    name = module_info.get('name')
    module_name.append(name)
print(module_name)
print("module_num:", len(module_name))
```

```shell
# 注意对比instances_train2017.json里面模型名称的顺序，与CLASSES和coco_classes里面的顺序保持一致。
```

### 2、修改 faster_rcnn_r101_2x_coco.py

`mmdetection/xianjin/faster_rcnn_r101_2x_coco.py`

修改46行，`num_clasess`的指，新增1个，就+1

### 3、修改 coco.py

`mmdetection/mmdet/datasets/coco.py`

CLASSES = ()，在里面添加模型名称

### 4、修改 class_names.py

`mmdetection/mmdet/core/evaluation/class_names.py`

`coco_classes` 里面添加模型名称

## 八、缓存清理

删除 mmdetection/build 目录

```python
python setup.py install
```

## 九、训练模型

### 指定自己配置的训练模型
```shell
python tools/train.py xianjin/faster_rcnn_r101_fpn_2x_coco.py --gpus 1
```

### 查看训练结果的测试集结果

```shell
python tools/train.py xianjin/faster_rcnn_r101_fpn_2x_coco.py xianjin/epoch_24.pth --show
```

### 查看训练结果的准确度
```shell
python tools/analysis_tools/analyze_logs.py plot_curve xianjin/20210530_011907.log.json --keys acc
```

## 十、快捷操作

```shell
python run.py
```

run.py 整合了以上所有的操作。
