**Linux基础知识**

**一、Linux系统**

**1.Linux概述**

（1）Linux系统是由Linux内核加上一些应用程序组成的一套能够有效管理计算机系统的软件。

（2）进程：是应用程序的执行态，一个程序执行时会生成一个进程ID，又称PID号。

**2.Linux安装**

(1) 下载centos6.0的镜像文件，下载安装虚拟机软件（vmware/virtualbox）

(2) 在虚拟机软件上新建一个虚拟机，根据操作步骤，选择centos镜像文件，安装Linux系统。

(3) 安装好之后，用ifconfig，查看虚拟机IP地址。

(4) 若非192.168.1开头的，需要进行设置

① su -

② service network restart

③ ifup eth0

(5) Linux连接工具：安装xshell和xftp

① ssh 192.168.1.38

② ssh mikigo@192.168.1.38

 

**二、linux基础命令**

**（一）用户与身份**

**1、用户**

(1) Root 是管理员，光标前为#

(2) 其他名称为普通用户，光标前为%

**2、切换用户**

(1) su - root表示切换到管理员权限，需要输入密码，也可以直接用su -

(2) u - 其他用户名，表示切换到其他用户

**（二）目录的基本操作**

**1. ls 列出当前目录的内容(list)**

① ls -l 详细列出当前目录的列表 如在root目录下ls -l 会显示目录下所有的文件。

② ls -l -h 详细列出当前目录的列表，并且能够优雅的显示（可以看出文件大小）

③ ls -lh 同ls -l -h

④ ls -a (all)显示所有文件（包含隐藏文件）

⑤ ls -A (almost all) 显示所有文件，不显示.和..(不显示当前目录和当前目录的父目录)

⑥ ls --color=never 去掉颜色

⑦ ls -R /root 表示将root下所有的文件显示出来（包含子目录）

**2. cd 改变工作目录**

① cd 不加任何路径，表示快捷直接回家

② cd - 表示返回上个切换的目录

③ cd  /root/tmp/test 表示切换到test目录下。

**3. pwd 显示当前共工作目录的绝对路径**

**4. mkdir创建一个空目录**

① mkdir a b c 同时创建多个并列文件夹

② mkdir -p zhang/li/wang 同时创建多个存在层级关系的文件目录。

③ mkdir -p -v zhang/li/wang 可显示命令的执行过程。

**5. rmdir 只能删除空目录**

**6.通配符**

1、* 代表任意一个（1个或多个）

2、？代表1位，且必须为1位

3、[  ]表示括号中的每一个

(1) ls test[ab] 结果是 testa testb

(2) ls test[0-6] 结果是 从最后一位是0-6取匹配

(3) ls test[a-Z] 结果是 从最后一位是所有字母去匹配

(4) [^a-c] 表示取反，即非a-c的字符

4、{  }字符串，字符串之间用,间隔 （{sta,atb,stc}）

**（三）文件的基本操作**

**1. touch 新建文本文件**

① touch test.txt 表示新建了一个test.txt 文档

② vim test.txt 表示编辑test这个文档

**2.rm 删除文件**

① rm -rf filename  表示删除某个文件

**3.cp 文件复制**

① cp  /root/test.txt  /tmp/hello.txt（表示将test文件复制到tmp目录中,并命名为hello）

② cp -r text2 /tmp 复制目录，需要加 -r

③ scp -r [root@192.168.1.47:/root/test2](mailto:root@192.168.1.47:/root/test2) /tmp 表示远程复制目录到tmp下（对方的地址、用户名和密码）

④属性不变，cp  -p 

**4.mv 文件移动**

① mv  /root/test.txt  /tmp  表示移动test文件到tmp目录下

② mv xxx.zip hhh.zip 表示将某个文件重命名

**5.查看文件**

**1、tail -f filename 监控文件（tail -2f filename 表示监控文件后2行）**

2、tail -n filename 查看尾部n行，如果无选项，默认10行。

3、head -n filename 从上到下查看n行，如果无选项，默认10行。

4、cat filename 查看文本

5、cat -n filename 查看文档并编号

6、cat -b filename 查看文档内容，并去除空行编号

7、more filename 显示更多内容，空格翻下一页，回车翻下一条

8、less filename 显示文档内容，支持上下翻页，退出“q”

**6.vim 文件编辑**

6.1、进入编辑模式

(1) i 表示在光标当前位置编辑。

(2) a表示在光标当前位置的下一个字符开始编辑。

(3) o表示在光标下一行开始编辑。O光标上一行开始编辑。

6.2、命令行模式

(1) 0（零）跳到行首（不能跳到行首前的空格处）

(2) ^ 跳到行首（包括空格）

(3) $ 跳到行尾

(4) gg 跳到第一行的行首

(5) GG 跳到最后一行的行首

(6) yy 复制单行，5yy或y5y复制5行

(7) p 粘贴，如果复制是1行，则p到下一行，如果复制的是10行，则p粘贴10行

(8) dd 删除一行，5dd删除5行

(9) cc 删除一行，并进入删除模式

(10) x 删除字符

(11) dw删除单词

(12) 查找/，n向下翻，N向上翻

(13) w 按单词走

(14) u 撤销

6.3、底行模式

(1) :wq 保存并退出

(2) :q! 强制退出

(3) /查找

(4) set ic 忽略大小写

(5) set noic 取消忽略大小写

(6) set nu 内容编号

(7) set nonu 取消内容编号

(8) %s/spool/linux/g 表示将所有的spool 替换为linux，g是固定用法。

**7.文件压缩和解压缩**

**（1）gzip**

(1) gzip  file.gz  file1,压缩单个文件，以.gz 结尾，压缩后源文件不在了

(2) 解压：gzip -d file.gz

(3) gunzip 同gzip -d

**（2）bzip2**

(1) bzip2  file.bz2  file1  压缩单个文件，以.bz2结尾

(2) 解压：bzip2 -d file.bz2

(3) bunzip2 同 bzip2 -d

**（3）xz**

(1) 压缩：xz  file.xz  file1  压缩单个文件，以.xz结尾

(2) 解压：xz -d file.xz 或 unxz file.xz

**（4）zip**

(1) 压缩：zip  file.zip  file1 file2

(2) 解压：unzip  file.zip

(3) 源文件还在

**（5）****tar (打包)**

(1) 压缩：tar  -czvf  file.tar.gz file1 file2

**(2) gz解压：tar  -xzvf  file.tar.gz  -C  Desktop 表示解压到桌面目录下**

**(3) z表示gzip，j表示bzip2，J表示xz**

**(4) bz2解压：tar  -xjvf  file.tar.bz2**

**(5) xz 解压：tar  -xJvf  file.tar.xz**

**（四）路径**

1．绝对路径：是以/开头，从根目录开始一级一级往下写（/root/tmp/test）

2．相对路径：不以/开头，从当前路劲开始(tmp/test)

**（五）文件访问权限**

1、权限分4部分，第1位是文件类型，第2-4位是u（user）用户权限，第5-7位是g（group）组权限，第8-10位是o（other）其他用户权限，第2-10位为a（all）

2、文件类型有，-普通文件，d目录，l软链接

3、u g o  分别有 r w x（读、写、执行）权限。

4、文件增加权限:chmod u+w file (+  -  =)

5、文件赋权：chmod 754 file  (r 4,w 2 x 1)

6、给目录加权限，要给目录下所有的文件加权限，才有意义

chmod -R o+w test1

7、改变拥有者：chown admin hello.sh

8、改变组： chown :admin hello.sh

9、改变拥有者和组： chown ftp:users hello.sh 表示将hello改用户为ftp,组改为users

**（六）用户管理和组管理**

1、新增用户： useradd name

 passwd name

2、删除用户：userdel name

 passwd name

3、添加组：groupadd group_name

4、查看组：cat  /etc/group

5、添加组成员： gpasswd  -a  peter  peter-group 表示添加peter到peter-group这个组里面。

6、删除组成员： gpasswd  -d  peter  peter-group 表示将peter从peter-group组中删除。

**（七）文件查找**

**find  绝对路径 选项 参数**

(1) find  /home  -name  miki 表示根据文件名miki在home下查找

(2) find  /home  -iname  miki 表示根据文件名miki在home下查找，且不区分大小写

(3) find  /home  -type  f 表示按文件类型查找

(4) find  /home  -type  d 表示按目录类型查找

(5) find  /home  -user  miki 表示根据用户miki去查找

(6) find  /home  -size  +-10k 表示根据文件大小去查找（大于或小于10k）

(7) find  /home  -maxdepth 1 表示根据最大深度1层查找

(8) find  /home  -mtime +-3 表示根据超过3天未修改，或小于3天未修改查找

(9) find  /home  -name  test  -exec  rm  -rf  { } \; 将取出的行删除。

**（八）帮助命令**

1、man 命令 

**查外部命令，查内部命令时会把所有的命令列出**

2、help 命令 

**查找内部命令**

**（九）进程管理**

**1、ps -ef** 

进程快照 

\## top命令：实时进程

\## free命令：查看系统内存情况

**2、grep 按行过滤，语法：grep 选项 参数**

(1) grep  -i  miki 表示忽略大小写

(2) grep  -v  miki 表示取反

(3) grep  “^miki” 表示从miki字符开始的行

(4) grep  “miki$” 表示以miki字符结尾的行

(5) grep  “^$” 表示取空行

(6) grep  -n  miki 显示行号

(7) grep  -B2  miki 表示取前两行，用A表示往后取

(8) grep  -A2  -B2  miki 表示取前后两行

**3、cut -d “：”-f 1-3** 

表示按列截取，以：划分位列，取1-3列

**4、查看端口号**

netstat  -tupnl  | grep 服务

**5、kill 结束进程**

（1）kill filename或kill -15 filename 是建议结束进程。

（2）kill  -9  filename 表示强制结束进程。

**（十）磁盘管理**

1. 系统服务

① uname -a 查看操作系统名称及环境

② hostname 查看服务器名称

③ cat /etc/redhat-release 查看系统的具体版本

2. 系统磁盘

① df -h 查看磁盘分布信息

② du -h 查看文件占用磁盘情况

3. 系统启动

① 关机

shutdown -h 20:00/now

② 重启

shutdown -r  或 reboot

**（十一）软件安装**

**1、二进制安装**

**(1) rpm包（redhat package management）**

① 安装：rpm  -ivh  程序包

② 卸载：rpm  -e

③ 查看是否安装： rpm  -qa

④ 统计多少个安装程序：rpm  -qa | wc  -l

⑤ 查看安装信息： rpm  -qi

⑥ 列出安装目录文件：rpm  -ql

⑦ 列出配置文件： rpm  -qc

⑧ 安装前查看包信息：rpm  -qpi

**(2) yum**

① 安装：yum install -y 安装包

② 卸载：yum remove 或 yum erase

**2、源代码安装**

(1) 安装步骤

① 解压后找到configure

② 执行：./configure  --prefix=/usr/local/目录名

③ make

④ make install

(2) 安装后需要指明路径（配置环境变量）

① ln  -s  /usr/local/lrzsz  /usr/lacal/bin

(3) 卸载：rm -rf

**三、shell程序设计**

**（一）输入输出**

**1.管道 |**

（1）表示将前面命令的结果，作为后面命令的参数

（2）cat -n test | head -12 | tail -2 表示取第11 和12行

（3）-v 显示控制字符，-n 对输出行进行编号，-b 和 -n一样，但空白行不编号。

**2.echo**

（1）echo $PATH  | tr “:” “\n” 表示输出以：分割换行的格式

（2）echo –n “hello world” 不换行

（3）echo “${PATH}abc“ 表示输出变量PATH的值，后面跟abc

（4）echo “now is $(date)” 或 echo “now is `date`” 命令替换

（5）echo ‘now is ${PATH}’ 单引号可以去掉$的功能，直接输出单引号内的字符

（6）echo –e “hello\nworld” –e 使引号内转义符生效

（7）\ 转义符，使后面一个字符失效

**3.read 定义一个变量**

（1）read username age

​     Peter\tong 12

（2）read –p “please input your name :” name 表示在输入变量时给出相应的提示。

**4.tee**

tee -a file 表示将文件追加到末尾  eg： ls | tee xxx.txt

**5.重定向**

（1）ls > file 表示重定向到文件中，会覆盖原有内容

（2）ls >>file 表示追加到文件末尾

（3）ls 2>file 表示标准错误重定向到文件中，会覆盖原有内容

（4）ls &>file 表示标准输出和标准错误一起重定向到文件中

（5）ls 1>file1 2>file2 表示标准输出重定向file1，标准错误输出重定向到file2

**（二）shell后台执行命令**

**1. cron 定时任务**

（1）管理员在 /etc/crontab里面可以编辑定时任务

（2）第一列表示min，第二列表示hou，第三列表示day，第四列表示mon，第五列表示	week，第六列表示要运行的命令。比如5，25 15 * * *，表示每天的15时的5分和25分运行脚本。

（3）普通用户创建为，执行命令crontab * * * * * 加选项 -e 编辑 ,-l 查看任务

**2.at**

(1) at 时间  做什么

(2)at –l 或 atq查看定时任务

(3)atrm 或 at –d 删除任务

**3.&**

（1）将某个运行的命令，放到后台执行。

（2）nohup 命令 $ 比如：nohup sleep 500 $

**（三）shell变量和参数**

**1.系统变量**

（1）**系统变量都是大写**

（2）**设置环境变量：export 将普通变量变成系统变量**

**var_name=value;export var_name**

变量命令要求：只能以字母、下划线、数字组成，且不能以数字开头

（3）env 查看所有的系统环境变量

（4）unset var_name 清除系统环境变量

**2.用户变量**

（1）设置用户变量：

**var_name=value**

（2）**清除变量：set var_name**

（3）**set 显示用户所有变量**

（4）source /etc/profile 让profile生效

（5）eho ${name:=peter} 表示如果name存在就显示name的值，如果不存在就显示peter

**3.位置变量**

（1）向shell脚本传递参数

（2）#！/bin/bash

echo “The script name is : $0”

echo “The script name is : $1”

$0表示脚本名称本身（包含前面的路径），$1表示第一个参数，以此类推。

echo ”The script name is : `basename $0`“ 表示仅显示脚本名称，但不包含前面的路径。

   /tmp/first.sh 仅显示first.sh

**4.特定变量**

echo $? 检查上一条命令是否执行成功，返回值为0即成功，返回非0即失败。

**四、shell程序设计流程控制**

**（一）test测试命令**

1.文件测试

1) [ -f file.txt ] 判断file是否为普通文件
2) [ -d file ] 判断file是否为目录
3) [ -s file ] 判断file文件长度大于0

2.逻辑操作符

1) -a : [ -f file –a –d file1 ] 表示判断两个条件是否同时满足。（与运算）
2) -o : [ -f file –o –d file1 ] 表示判断两个条件是否右一个满足。（或运算）
3) ! : 表示取非，比如[ ! –f file ]

3.数值测试

1) -eq 数值相等 ，比如[ “$num” –eq “100” ]
2) -ne 数值不等
3) -gt 第一个数大于第二个数
4) -lt 第一个数小于第二个数
5) -le 小于等于
6) -gt 大于等于

**（二）expr 简单计算**

1.expr 10 + 10 运算符两边要右空格

2.sum=`expr 9 +4 `

3.let sum=5+5

  echo $sum

**（三）if条件判断**

1.格式： if 条件;

then 命令

elif 条件

then 命令

else

​    命令

   fi

2.if条件判断有真假，真则写在then后面，假则写在else后面，其中真假都可以继续嵌套if语句。

3. num=$1

if [ “$num” = “100” ];

then echo “$sum”

 else

  echo “wrong number”

**（四）for循环**

1.格式： for 变量名 in 列表

do

命令1

命令1

   done

2.eg: for mikigo in 1 2 3 4 5

  do

   echo $mikigo

  done

**（五）while和until 循环**

1.while 条件

do

  命令1

done

2.while 是判断条件为真时执行命令，until是判断条件为假时执行命令，语法格式都一样。

3.while [ $num –lt 5 ]

do

  echo “$num”

  let num=$num+1

done

**（六）break 和 continue**

1.break 是跳出离它最近的一个循环

2.continue 是结束这一次循环，继续下次循环

3. while num=0

do

 if [ “$num” –eq 2 ];

then

 	continue

else

echo “$num”

 let num=$num+1

fi

done

**（七）case条件选择**

1.case 值 in

  模式1）

​    命令1

​     ；；

模式2）

​    命令2

​    ；；

  esac

2. echo “ABCDE” | tr “A-Z” “a-z” 表示将所有的大写字母替换成小写字母。

**（八）备份数据库脚本**

1.新建一个sh脚本文件（vim backup.sh）

\#!/bin/bash

DB_NAME=5kcrm

DB_USER=root

DB_PWD=

Now=$(date "+%Y_%m_%d %H:%M:%S")

File=backup-$Now.sql

mkdir /root/backup

cd /root/backup

mysqldump -u${DB_USER} -p${DB_PWD} ${DB_NAME}>${File}

echo 'this database is backup ok'

2.赋权

chmod +x backup.sh