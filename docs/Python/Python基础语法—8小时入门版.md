
# Python基础语法—8小时入门版

```shell
# =============================
# Author : mikigo
# Time   : 2020/10/10
# =============================
```

##  一、Python基础

### **（一）输入输出**

**1. print**

```python
（1）print("hello world") 括号表示调用函数print，括号内的字符串用引号引起来。

（2）print("hello","world","mikigo") 可接受多个参数。

（3）print(name）不加引号表示调用变量。

（4）print(100+200) 不加引号，表示直接运算。
```

**2. input**

```python
（1）input() 输入，光标会等待键盘输入。

（2）input("请输入内容") 括号内建议输入提示信息。

（3）input 输入的值都会被当成字符串，包括数字。
```

### **（二）数据类型**

```python
1. 整数 int 没有小数点。

2. 浮点数 float ：有小数点。

3. 布尔值 bool ：True 或 False 。注意首字母大写。

4. 空值 None :空值，但和0有区别。

5. type() 查看数据类型（isinstance）。
```

### **（三）变量、表达式**

**1. 变量赋值**

 （1）`name="mikigo"` 表示将 `mikigo` 这个字符串赋值给变量 `name`，注意要加引号，不加引号会被认为是一个变量

 （2）a,b,c=7,8,9 多元赋值，表示将值一一对应的复制到等号前面的变量，但位置的个数一定要一致。

 （3）数据类型的转换

```python
 - str(age) 表示将变量age转换成字符型

 - int（1.5）表示将float转换成int（取整为1）

 - float(6) 表示将int转换成float
```

**2. 表达式**

```python
（1）+ - * /

（2）% 表示取余数

（3）// 表示取商数

（4）** 表示次幂 ，比如10**5 表示10的5次幂
```

### **（四）字符串 string**

**1.格式化字符串**

```python
（1）%d（data） 表示数字站位

（2）%s（string） 表示对字符串站位

（3）%r 任何类型都可以接收，但字符串最终打印出来有引号。

（4）格式：print("%s = %d" % （age,19）)

（5）"mikigo{}".format(("good",))

（6）f"mikigo{good}"
```

**2.字符串操作**

（1）字符串相加，比如：`"mi" + "ki" > miki`；

（2）星号相乘，比如：`2 * "mi" > mimi`；

（3）[ ] 表示通过索引截取字符，第 1 个字符索引是 0 ；

（4）[ : ] 表示截取字符串 比如：[2:4] 表示从索引 2 开始，截取到索引 3（不包含 4 ）；

（5）in 表示 in 后面字符串中是否包含 in 前面的字符，比如：`"i" in "miki"  >> True；`

（6）not in 用法与 in 类似但是取反；

（7）r/R 表示所有字符都按照字面意思来使用。比如：`print(r"hello\nmikigo")` 换行字符 \n 不起作用，直接输入引号内的字符串。

**3.字符串的常见函数方法**

（1）len(str) 返回字符串的长度；

（2）count 计数；

```python
- "mikigo".count("mi") 直接跟字符或字符串，则返回字符出现的次数。

- "mikigo".count("i",2,10) 表示在索引2到10之间（不包含10），返回字符出现的次数。
```

（3）startswith 或 endswith 以什么开始或以什么结束；

```python
- "mikigo".startswith("m") 表示判断是否以字符m开始，> True

- "mikigo".endswith("m") 表示判断是否以字符m结束，> False
```

（4）find 查找字符或字符串，返回索引位置，如果找不到会返回 -1；

```python
- "mikigo".find("i") 表示找出字符i在字符串中第一次出现的索引位置，> 1

- "mikigo".rfind("i") 表示从右开始找出字符i在字符串中第一次出现的索引位置，> 3
```

（5）index 用法同 find，区别在于，找不到时会报错；

（6）strip 删除或截掉；

```python
- " mikigo ".strip() 删除前后的空格

- " mikigo ".rstrip("o") 删除右边的字符o

- " mikigo ".lstrip("m") 删除左边的字符m
```

（7）replace 替换

```python
- "mikigo".replace("i","oo") 表示将字符串中的所有字符i替换称字符串oo

- "mikigo".replace("i","oo",1) 表示将字符串中的字符i替换为oo，只替换一次
```

（8）join 加入：`"miki".join("ab")  >> "amikib"` 每个字符拆开，加入某个字符或字符串。

（9）split 以分隔符截取

```python
- "mikigo".split("i") 表示以字符i作为分隔符，将字符串进行分隔。

- "mikigo".split("i",1) 表示以字符i作为分隔符，以第1个i作为字符串的分隔符 进行分隔。

- "mikigo\nhello".splitlines() 或  "mikigo\nhello".splitlines(keepends=False) 表示按行（"\r","\n","\r\n"）分隔（不包含换行符）。

- "mikigo\nhello".splitlines(keepends=True) 表示以\n换行，且包含换行符。

- 扩展: 多种方式分割字符串  re.split('a|b', 'fdasfweqgasfewaq')
```

### **（五）列表（list）**

**1.list基本操作**

```python
（1）列表（list）用[ ]表示，是有序，可变，可指定位置取值的。

（2）列表里面的元素，可以是任意数据类型，包括列表、None、bool

（3）同一列表中可存放不同的数据类型
```

**2.切片**

```python
（1）lst[index] 取单个元素，直接跟索引。比如 lst[2]，表示取索引 2 的元素；

（2）lst[0:2] 取一个区间。表示取索引 0 到 1 的元素；

（3）lst[0:5:2] 表示按步长 2 去取索引 0 到 4 之间的元素；

（4）lst[-1] 表示取最后一个；

（5）lst[::-1] 表示将一个列表反向排序。
```

**3.list常见的函数和方法** 

**（1）函数**

```console
1）len(list) 列表的长度，即列表中元素的个数；

2）max(list) 相同的数据类型取最大值。
```

**（2）方法**

```python
1）list.append(obj) 在列表末尾添加新的对象。list.append("ab"),表示在末尾加入字符串 "ab"，但 append 一次只能增加一个元素；

2）list.count(obj) 统计某个元素在列表中出现的次数；

3）list.extend(seq) 在末尾追加另一个序列。追加的是一个列表，不能是单个元素。比如 list.extend([123])；

4）list.index(obj) 找出某个元素的第一个索引位置；

5）list.insert(index,obj) 将对象插入到列表（位置，元素）；

6）list.pop(index) 删除某个位置的元素（默认删除最后一个）。比如 list.pop(1) 表示删除索引1的元素，且返回元素的值；

7）list.remove(obj) 删除列表中的某个元素的第一个，修改列表本身；

8）list.reverse() 反向排序；

9）list.sort() 重新排序；

10）list.clear() 清空列表；

11）list.copy() 复制列表。
```

### **（六）元组（tuple）**

 定义：以小括号括起来的有序列表，但不能修改。

 ```python
 a = (2,3,4,5)
 ```

### **（七）字典（dict）**

1.定义：字典是用大括号括起来，由键值对（key:value）组成的，且是无序的。

2.key 是唯一的，一般赋值为 string，value 可以是任意数据类型

**3.常用操作**

```python
（1）dt["key"] 根据键读取值

（2）dt["old_key"]="new_value" 根据键修改值

（3）dt["new_key"]="new_value" 新增键值对

（4）len(dt) 返回元素的量（键值对）
```

**4.dict常用方法**

```python
（1）key in dict 判断键是否在字典中

（2）dict.items() 返回列表，列表由元组组成，每个元组由一个键值对将键和值拆分为两个字符串组成。

（3）dict.keys() 将所有的键组成一个列表。

（4）dict.values() 将所有的值组成一个列表。

（5）dict1.update(dict2) 将字典2中的键值对添加到字典1中

（6）dict.get(key,default=None) 返回指定键的值，如果值不存在，返回default值。比如：dict.get("name","peter") 如果字典中有name这个键，则直接返回其对应的值，如果没有这个键，则返回"peter"

（7）dict.setdefault(key,default=None) 和get一样会返回指定键的值，但若键不在字典中，会添加成为新的键值对。比如：dict.setdefault("name","peter")，如果字典中有name这个键，则返回其对应的值，如果没有，则会将定义的值，添加到字典中。

（8）dict.pop(key,default=None) 删除键对应的值，key不存在返回default值。

（9）dict.copy() 浅复制

（10）dict.clear() 清除所有元素
```

## **二、过程控制**

### **（一）条件语句**

1.句式：

```python
if 条件判断：（缩进和冒号）
    print("字符串")
else:
    print("字符串")
```

 2.else 可以不要，语法上没有问题

 3.运算符

 (1)  `< , <= , > , >= , == , !=`

 (2）`and , or , not , in , not in, is`

### **（二）循环语句**

1.while

```python
while 判断条件：
    语句
else ：
    语句
```

 	break 终止循环语句
 	
 	continue 结束本次循环，继续进行下一轮循环。

2.for语句（遍历序列的元素）

```python
for i in [1,2,3,4]：
    print(i)
```

- in 后面可以跟元组、列表、字符串，但跟字典时只能取到字典中的键（key）。

- range(函数)
  - range(3) 表示从索引0，取到索引2（开区间）
  - range(1,4) 表示从索引1，取到索引3
  - range(1,10,2) 表示从索引1，取到索引10，步长为2

## 三、函数

### （一）定义

函数是可重复使用的，具有一定功能的代码段。

def 函数名（参数1，参数2，····）

  ```python
def add(a,b):
    c = a + b
    print(c)
  ```

### （二）返回值

调用函数后，将执行结果返回给调用者。
```python
def add(a,b):
    c = a + b
    return c
```
\>>x=add(1,2)  # 返回一个c的值赋给x，如果返回值有多个，而变量只有1个，则会生成一个元组。也可以用多个变量对应多个返回值，即多元赋值。

### （三）参数

#### 1、位置参数(形参)

```python
def func(name, age):
    print(name, age)
```
位置参数时根据位置顺序传入函数，调用函数时必须与定义时的参数数量一致。

#### 2、默认参数

-  def func(name, age=18):      print("a未被定义")  # 参数在定义的时候就赋值的

- 默认参数在调用的时候如果不传入，则会使用默认参数，如果给传递了参数，则值会被覆盖。

#### 3、可变参数

```python
def func(*args):
    sum = 0
    for n in args:
        sum = sum + n
        return sum
```
  \>>func(1,2,3,···)  传入的参数数量可变，会自动组装称一个元组，如果传入0个参数，结果时返回一个空元组。

- 如果传入的参数是一个元组，调用的时候在函数括号内加*号（参数解构）

  tp=（1，2，3，4）

  resule = add(*tp)

#### 4、关键字参数（键和值）

```python
def func(**kwargs):
    print(kwargs)
```

  \>>func(name="peter")   # 结果是打印一个字典{"name"："peter"}

- 如果传入的参数是一个字典，调用的时候在函数括号内加**

  \>>dct = {"eat1":"酸辣粉","eat2":"螺狮粉"}

  \>>func(**dct)

#### 5、组合参数

顺序为**位置参数，可变参数，默认参数，关键字参数**

```python
def func(name, age, *args, gender=’男’, **kwargs)
```

## 四、类（class）

### （一）类的实例

1.类的实例是对象，一个实例包含属性（有什么）和方法（能做什么）。

2.类的声明：class 类名():  类名单词首字母大写，如果是多个单词，单词与单词之间不空格，直接挨着写，但每个单词首字母需要大写。

3.定义类的属性和方法

```python
class Person():

    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def run(self, food):
        print("%s都%d岁了,天天吃%s" % （self.name, self.age,food）)
```

（2）方法调方法或方法调属性等，内部调用都要加self。  ②

（3）调用外部变量时，不加self。

（4）调用

```python
① 实例化：x = Person("peter",18)

② print(x.name) 调用类的属性

③ print(x.run("肉"))
```

### （二）继承

子类继承父类的属性和方法

```python
class Student(Person):  #继承时括号内直接写父类的类名
    pass #完全继承父类的属性和方法。
```

```python
class Student(Person):

    def __init__(self,name,age,cno)
        Person.__init__(self,name,age)  
        self.cno = cno #在父类的基础上新增属性，需要先将父类指定进来。否则新增属性会将父类的属性覆盖。
        
    def run(self):
        r = Person.run(self)
        return r  # 在父类的基础上新增方法，需要先指定父类的方法。
```

方法重新定义后，调用的时候，默认先去调用子类的方法，然后再去调用父类的方法。

### （三）访问限制

1．访问限制可以使，类内部的属性和方法，不能外部随便访问。用法是在属性或方法前面加双下划线，表示私有属性。

2．访问限制，不能被外部随便访问，但可以被内部调用，私有属性可以用方法调用，私有方法，可以定义其他方法调用。

```python
class Person():
    def  __init__(self,name):
        self.__name = name
        
    def  __eat(self,food):
        return "%s爱上吃%s"% (self.__name,food)
```

### （四）编码规范

1．缩进，4个空格的缩进，空格和tab不能混用（tab仅在编辑器中可使用）。

2．类名的单词以大写字母开头。

3．函数和类的属性命名以小写，用下划线连接

4．所有的命名都应采用有意义的英文单词，多单词由下划线连接。

## 五、模块

### （一）引入模块

（1）import 后面直接跟模块名或类或函数。

```python
import time
```

（2）from 路径 import 类或函数 #路径最好用绝对路径。

```python
from model.A import add
```

### （二）安装三方库

（1）sudo pip3  install  pymysql(三方库名)  # 在命令行直接输入即可。

（2）在 pycharm 里面，点击 file，选择 setting，选择 Project，选择 Project Interpreter，在右上角点 + 号，输入库名即可安装。

（3）如果是需要下载的三方库，下载后查看文件包里面的 readme 文件，根据描述进行安装。

## 六、异常处理

### （一）try语句

（1）try ... except...except 表示当程序运行错误后，被 except 捕捉到，返回一个可定义的信息，且不会影响后续语句的执行。每个 except 后面跟不同的返回信息。
```console
try:
    print(a)
    10/0
except NameError:
    print("a未被定义")
except ....
```


（2）try ...except...finally 同（1）一样，但 **finally** 后的语句，无论是否发生异常，都会执行。

（3）try...except...else 同（1）一样，但 **else ** 后的语句，是在没有发生异常的情况才会执行。

### （二）抛出异常

① raise NameError("这是一个名称错误")

### （三）常见的异常

① AssertionError  assert（断言）语句失败。

② AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有x这个属性。

③ IOError 输入/输出异常，基本上是无法打开文件。

④ ImportError 无法引入模块或者包，基本上是路径问题。

⑤ IndentationError 语法错误，代码没有正确对齐。

⑥ IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]。

⑦ KeyError 试图访问字典里不存在的键。

⑧ Kerboardinterrupt  Ctrl+C被按下，主要针对无限循环。

⑨ NameError 使用一个还未被赋值予对象的变量。

⑩ SyntaxError 代码非法，代码不能解释。

⑪ TypeError 传入对象类型与要求的不符。

⑫ UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另一个同名的全局变量，导致你以为正在访问它。

⑬ ValueError 传入一个调用者不期望的值，即使值的类型是正确的。

⑭ FileNotFoundError 试图打开一个不存在的文件或目录。

## 七、文件读写

### （一）以读的形式打开，并能写（r+）

1.

```console
>> f = open("test.txt","r+")
>> f.write("xxx")
>> f.flush()
>> f.close()
```

2.光标会放在文件开头，输入的输入会覆盖开头

### （二）以写的形式打开，并能读(w+)

1.

```console
>> f = open("test.txt","w+")
>> data = f.read()
>> print(date)
```

2.若文件已存在会将其覆盖，若文件不存在，会新建文件。

### （三）追加模式（a+）

1.

```console
>> f = open("test.txt","a+")
```

2.光标在文件的末尾，写入会追加到末尾，若文件不存在，会新建文件。

```python
with open("test.txt","a+",encoding="utf-8") as f:
    f.write("我是中文")
    f.flush()
```
