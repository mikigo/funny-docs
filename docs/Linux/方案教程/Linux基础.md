---
counter: True
---

# Linux&Shell基础

```shell
# =============================
# Author : mikigo
# =============================
```

## linux基础命令

### 用户与身份

#### 1、用户

(1) Root 是管理员，光标前为#

(2) 其他名称为普通用户，光标前为 $

#### 2、切换用户

(1) su - root 表示切换到管理员权限，需要输入密码，也可以直接用su -

(2) u - 其他用户名，表示切换到其他用户

### 目录的基本操作

#### ls 列出当前目录的内容(list)

```sh
# 详细列出当前目录的列表 如在root目录下ls -l 会显示目录下所有的文件。
ls -l 
# 详细列出当前目录的列表，并且能够优雅的显示（可以看出文件大小）
ls -l -h 
# 同ls -l -h
ls -lh 
# (all)显示所有文件（包含隐藏文件）
ls -a 
# (almost all) 显示所有文件，不显示.和..(不显示当前目录和当前目录的父目录)
ls -A 
# 去掉颜色
ls --color=never 
# 表示将root下所有的文件显示出来（包含子目录）
ls -R /root 
```

#### cd 改变工作目录

```sh
# 不加任何路径，表示快捷直接回家
cd 
# 表示返回上个切换的目录
cd - 
# 表示切换到test目录下
cd  /root/tmp/test 
```

#### pwd 显示当前共工作目录的绝对路径

#### mkdir创建一个空目录

```sh
# 同时创建多个并列文件夹
mkdir a b c 
# 同时创建多个存在层级关系的文件目录。
mkdir -p zhang/li/wang 
# 可显示命令的执行过程
mkdir -p -v zhang/li/wang 
```

#### rmdir 只能删除空目录

#### 通配符

1、* 代表任意一个（1个或多个）

2、？代表1位，且必须为1位

3、[  ]表示括号中的每一个

- `ls test[ab]` 结果是 `testa testb`
- `ls test[0-6]` 结果是 从最后一位是 `0-6` 取匹配
- `ls test[a-Z]` 结果是 从最后一位是所有字母去匹配
- `[^a-c] ` 表示取反，即非 `a-c` 的字符

4、`{  }` 字符串，字符串之间用,间隔 （`{sta,atb,stc}`）

### 文件的基本操作

#### touch 新建文本文件

```sh
# 新建一个test.txt 文档
touch test.txt
# 编辑test这个文档
vim test.txt
```

#### rm 删除文件

```sh
# 表示删除某个文件
rm -rf filename  
```

#### cp 文件复制

```sh
# 将test文件复制到tmp目录中,并命名为hello
cp  /root/test.txt  /tmp/hello.txt
# 复制目录，需要加 -r
cp -r text2 /tmp 
# 远程复制目录到tmp下（对方的地址、用户名和密码）
scp -r [root@192.168.1.47:/root/test2](mailto:root@192.168.1.47:/root/test2) /tmp
# 属性不变
cp  -p 
```

#### mv 文件移动

```sh
# 移动test文件到tmp目录下
mv  /root/test.txt  /tmp
# 将某个文件重命名
mv xxx.zip hhh.zip
```

#### 查看文件

```sh
# 监控文件（tail -2f filename 表示监控文件后2行）
tail -f filename
# 查看尾部n行，如果无选项，默认10行。
tail -n filename 
# 从上到下查看n行，如果无选项，默认10行。
head -n filename 
# 查看文本
cat filename 
# 查看文档并编号
cat -n filename 
# 查看文档内容，并去除空行编号
cat -b filename 
# 显示更多内容，空格翻下一页，回车翻下一条
more filename 
# 显示文档内容，支持上下翻页，退出“q”
less filename 
```

#### vim 文件编辑

1、进入编辑模式

-  `i` 表示在光标当前位置编辑。

-  `a` 表示在光标当前位置的下一个字符开始编辑。

- `o` 表示在光标下一行开始编辑。`O` 光标上一行开始编辑。

2、命令行模式

- `0`（零）跳到行首（不能跳到行首前的空格处）
- `^` 跳到行首（包括空格）
-  `$` 跳到行尾

- `gg` 跳到第一行的行首
- `GG` 跳到最后一行的行首
- `yy` 复制单行，5yy或y5y复制5行
- `p` 粘贴，如果复制是1行，则p到下一行，如果复制的是10行，则p粘贴10行
- `dd` 删除一行，5dd删除5行
- `cc` 删除一行，并进入删除模式
- `x` 删除字符
- `dw` 删除单词
- 查找 `/`，`n` 向下翻，`N` 向上翻

- `w` 按单词走
- `u` 撤销

3、底行模式

- `:wq` 保存并退出
- `:q!` 强制退出
- `/` 查找
- `set ic` 忽略大小写
- `set noic` 取消忽略大小写
- `set nu` 内容编号
- `set nonu` 取消内容编号
- `%s/spool/linux/g` 表示将所有的 `spool` 替换为 `linux` ，`g` 是固定用法。

#### 文件压缩和解压缩

1、gzip

- 压缩单个文件，以 `.gz` 结尾，压缩后源文件不在了

  ```sj
  gzip  file.gz  file1
  ```

- 解压

  ```sh
  gzip -d file.gz
  ```

- `gunzip` 同 `gzip -d`

2、bzip2

- 压缩单个文件，以.bz2结尾

  ```sh
  bzip2  file.bz2  file1
  ```

- 解压

  ```sh
  bzip2 -d file.bz2
  ```

- `bunzip2` 同 `bzip2 -d`

3、xz

- 压缩单个文件，以.xz结尾

  ```sh
  xz  file.xz  file1
  ```

- 解压

  ```sh
  xz -d file.xz
  # 也可以
  unxz file.xz
  ```

4、zip

- 压缩

  ```sh
  zip  file.zip  file1 file2
  ```

- 解压

  ```sh
  unzip  file.zip
  ```

- 源文件还在


5、tar (打包)

- 压缩

  ```sh
  tar  -czvf  file.tar.gz file1 file2
  ```

- gz解压

  ```sh
  # 解压到桌面目录下
  tar  -xzvf  file.tar.gz  -C  Desktop
  ```

- `z` 表示 `gzip`，`j` 表示 `bzip2`，`J` 表示 `xz`

- `bz2` 解压

  ```sh
  tar  -xjvf  file.tar.bz2
  ```

- xz 解压

  ```sh
  tar  -xJvf  file.tar.xz
  ```

### 路径

1、绝对路径：是以/开头，从根目录开始一级一级往下写（/root/tmp/test）

2、相对路径：不以/开头，从当前路劲开始(tmp/test)

### 文件访问权限

1、权限分4部分：

- 第 1 位是文件类型；
- 第 2-4 位是 `u（user）`用户权限；
- 第 5-7 位是 `g（group）`组权限；
- 第 8-10 位是 `o（other）`其他用户权限；
- 第 2-10 位为 `a（all）`；

```shell
$ ls -lh
drwxr-xr-x  3 root root     60 7月  13 09:27 user
```

2、文件类型：

- `-` 普通文件；
- `d` 目录；
- `l` 软链接；

3、`u g o`  分别有 `r w x`（读、写、执行）权限。

4、文件增加权限

```sh
chmod u+w file (+  -  =)
```

5、文件赋权

```sh
chmod 754 file  (r 4,w 2 x 1)
```

6、给目录加权限，要给目录下所有的文件加权限，才有意义

```sh
chmod -R o+w test1
```

7、改变拥有者

```sh
chown admin hello.sh
```

8、改变组

```sh
chown :admin hello.sh
```

9、改变拥有者和组

```sh
# 将hello改用户为ftp,组改为users
chown ftp:users hello.sh
```

### 用户管理和组管理

1、新增用户：

```shell
useradd -m name
# 指定的用户名设置密码
passwd name
```

2、删除用户

```shell
userdel name
```

3、添加组

```sh
groupadd group_name
```

4、查看组

```sh
cat  /etc/group
```

5、添加组成员：

```sh
# 添加 mikigo 到 mikigo-group 这个组里面。
gpasswd -a mikigo mikigo-group
```

6、删除组成员

```sh
# 将 mikigo 从 mikigo-group 组中删除。
gpasswd -d mikigo mikigo-group
```

### find 文件查找

```sh
find 绝对路径 选项 参数
```

```sh
# 根据文件名miki在home下查找
find  /home  -name  miki
# 根据文件名miki在home下查找，且不区分大小写
find  /home  -iname  miki
# 按文件类型查找
find  /home  -type  f
# 按目录类型查找
find  /home  -type  d
# 根据用户miki去查找
find  /home  -user  miki
# 根据文件大小去查找（大于或小于10k）
find  /home  -size  +-10k
# 根据最大深度1层查找
find  /home  -maxdepth 1
# 根据超过3天未修改，或小于3天未修改查找
find  /home  -mtime +-3
# 将取出的行删除。
find  /home  -name  test  -exec  rm  -rf  { } \; 
```

### 帮助命令

1、man 命令 

查外部命令，查内部命令时会把所有的命令列出

2、help 命令 

查找内部命令

### 进程管理

1、ps -ef 

进程快照 

`top` 命令：实时进程

`free` 命令：查看系统内存情况

2、grep 按行过滤，语法：grep 选项 参数

```sh
# 忽略大小写
grep  -i  miki
# 取反
grep  -v  miki 表
# 从miki字符开始的行
grep  “^miki”
# 以miki字符结尾的行
grep  “miki$”
# 取空行
grep  “^$”
# 显示行号
grep  -n  miki 
# 取前两行，用A表示往后取
grep  -B2  miki
# 取前后两行
grep  -A2  -B2  miki
```

3、剪切

```sh
# 按列截取，以：划分位列，取1-3列
cut -d “：”-f 1-3 
```

4、查看端口号

```sh
netstat  -tupnl  | grep 服务
```

5、kill 结束进程

（1）kill filename或kill -15 filename 是建议结束进程。

（2）kill  -9  filename 表示强制结束进程。

### 磁盘管理

1、系统服务

① `uname -a` 查看操作系统名称及环境

② `hostname` 查看服务器名称

③ `cat /etc/redhat-release` 查看系统的具体版本

2、系统磁盘

① `df -h` 查看磁盘分布信息

② `du -h` 查看文件占用磁盘情况

3、系统启动

① 关机

```sh
shutdown -h 20:00/now
```

② 重启

```sh
shutdown -r  或 reboot
```

### 软件安装

1、二进制安装

(1) rpm包（redhat package management）

- 安装：rpm  -ivh  程序包

- 卸载：rpm  -e

- 查看是否安装： rpm  -qa

- 统计多少个安装程序：rpm  -qa | wc  -l

- 查看安装信息： rpm  -qi

- 列出安装目录文件：rpm  -ql

- 列出配置文件： rpm  -qc

- 安装前查看包信息：rpm  -qpi


(2) yum

- 安装：yum install -y 安装包

- 卸载：yum remove 或 yum erase


2、源代码安装

(1) 安装步骤

- ① 解压后找到configure

- ② 执行：./configure  --prefix=/usr/local/目录名

- ③ make

- ④ make install


(2) 安装后需要指明路径（配置环境变量）

```sh
ln  -s  /usr/local/lrzsz  /usr/lacal/bin
```

(3) 卸载：rm -rf

## shell程序设计

### 输入输出

1、管道 `|`

（1）表示将前面命令的结果，作为后面命令的参数

（2）`cat -n test | head -12 | tail -2` 表示取第11 和12行

（3）`-v` 显示控制字符，`-n` 对输出行进行编号，`-b` 和 `-n` 一样，但空白行不编号。

2、`echo`

（1）`echo $PATH  | tr “:” “\n” `表示输出以：分割换行的格式

（2）`echo –n “hello world”` 不换行

（3）`echo “${PATH}abc“` 表示输出变量PATH的值，后面跟abc

（4）`echo “now is $(date)”` 命令替换

（5）`echo ‘now is ${PATH}’ `单引号可以去掉$的功能，直接输出单引号内的字符

（6）`echo –e “hello\nworld” –e` 使引号内转义符生效

（7）`\ `转义符，使后面一个字符失效

3、read 定义一个变量

（1）`read username age`

（2）`read –p “please input your name :” name` 表示在输入变量时给出相应的提示。

4、tee

`tee -a file` 表示将文件追加到末尾 

```sh
 ls | tee xxx.txt
```

5.重定向

- `ls > file` 表示重定向到文件中，会覆盖原有内容；
- `ls >>file` 表示追加到文件末尾；
- `ls 2>file` 表示标准错误重定向到文件中，会覆盖原有内容；
- `ls &>file` 表示标准输出和标准错误一起重定向到文件中；
- `ls 1>file1 2>file2` 表示标准输出重定向 `file1`，标准错误输出重定向到 `file2`；

### shell后台执行命令

1、cron 定时任务

管理员在` /etc/crontab` 里面可以编辑定时任务

- 第一列表示 min；
- 第二列表示 hou；
- 第三列表示 day；
- 第四列表示 mon；
- 第五列表示 week；
- 第六列表示要运行的命令；

比如：5，25 15 * * *，表示每天的15时的5分和25分运行脚本。

普通用户创建为，执行命令 `crontab * * * * *` 加选项 `-e` 编辑 ,`-l` 查看任务；

3、&

（1）将某个运行的命令，放到后台执行。

（2）`nohup 命令 &` 比如：`nohup sleep 500 &`

### shell变量和参数

1、系统变量

- 系统变量都是大写；

- 设置环境变量：export 将普通变量变成系统变量；

  ```sh
  var_name=value;export var_name
  ```

- 变量命令要求：只能以字母、下划线、数字组成，且不能以数字开头；

- `env` 查看所有的系统环境变量；

- `unset var_name` 清除系统环境变量；

2、用户变量

- 设置用户变量：

  ```sh
  var_name=value
  ```

- 清除变量：`set var_name`

- `set` 显示用户所有变量

- `source /etc/profile` 让 `profile` 生效

- `eho ${name:=peter}` 表示如果 `name` 存在就显示 `name` 的值，如果不存在就显示 `peter`

3、位置变量

- 向shell脚本传递参数

  ```sh
  #！/bin/bash
  echo “The script name is : $0”
  echo “The script name is : $1”
  ```

`$0` 表示脚本名称本身（包含前面的路径），`$1`表示第一个参数，以此类推。

```sh
# 仅显示脚本名称，但不包含前面的路径
echo ”The script name is : `basename $0`“ 
```

4、特定变量

```sh
# 检查上一条命令是否执行成功
echo $?
```

返回值为0即成功，返回非0即失败。

## shell程序设计流程控制

### test测试命令

1.文件测试

- `[ -f file.txt ]` 判断file是否为普通文件
- `[ -d file ] `判断file是否为目录
- `[ -s file ]` 判断file文件长度大于0

2.逻辑操作符

- `-a` 

  `[ -f file –a –d file1 ]` 表示判断两个条件是否同时满足。（与运算）

- `-o` 

  `[ -f file –o –d file1 ]` 表示判断两个条件是否有一个满足。（或运算）

- `! `

  表示取非，比如 `[ ! –f file ]`

3.数值测试

- `-eq` 数值相等 ，比如 `[ “$num” –eq “100” ]`
- `-ne` 数值不等
- `-gt` 第一个数大于第二个数
- `-lt` 第一个数小于第二个数
- `-le` 小于等于
- `-gt` 大于等于

### `expr` 简单计算

- expr 10 + 10 运算符两边要右空格

  ```sh
  sum=`expr 9 +4`
  let sum=5+5
  echo $sum
  ```

### if条件判断

- 格式：

  ```sh
  if 条件; then 
  	命令
  elif 条件
  	命令
  else
  	命令
  fi
  ```

- `if `条件判断有真假，真则写在 `then` 后面，假则写在 `else` 后面，其中真假都可以继续嵌套 `if` 语句。

```sh
num=$1
if [ “$num” = “100” ]; then 
	echo “$sum”
else
	echo “wrong number”
```

### for循环

- 格式

  ```sh
  for 变量名 in 列表
  do
      命令1
  	命令1
  done
  ```

- 举例

  ```sh
  for mikigo in 1 2 3 4 5
  do
  	echo $mikigo
  done
  ```


### while和until 循环

- 格式

  ```sh
  while 条件
  do
  	命令1
  done
  ```

- while 是判断条件为真时执行命令，until是判断条件为假时执行命令，语法格式都一样。

- 举例

  ```sh
  while [ $num –lt 5 ]
  do
      echo “$num”
      let num=$num+1
  done
  ```

### break 和 continue

- break 是跳出离它最近的一个循环

- continue 是结束这一次循环，继续下次循环

- 举例

  ```sh
  while num=0
  do
      if [ “$num” –eq 2 ]; then
      	continue
      else
      	echo “$num”
      	let num=$num+1
      fi
  done
  ```

### case条件选择

- 格式

  ```sh
  case 值 in
      模式1）
  		命令1；；
      模式2）
  		命令2；；
  esac
  ```