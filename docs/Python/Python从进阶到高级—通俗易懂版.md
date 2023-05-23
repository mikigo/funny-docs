# Python从进阶到高级—通俗易懂版

```shell
# ==================================
# Author : Mikigo
# Time   : 2021/12/23
# ==================================
```

## 一、简介

Python 进阶是我一直很想写的，作为自己学习的记录，过去自己在看一些代码的时候经常会困惑，看不懂，然后自己去查资料、看书籍，慢慢的一个个弄懂，经常沉浸其中。关于 Python 高级语法的资料、书籍不少，详细是详细，但是总感觉写的太复杂，学习有难度，而且不能使人印象深刻。

“`TLDR`” 是流行的互联网行话，意思是“太长不读（ to long didn't read ）”。其实很多内容的核心知识就那么一点，细枝末节的东西蛮多，描述词句也很官方很晦涩，很难读懂，给人感觉就是每个字我都认识，怎么放到一起就不认识了。通俗易懂版就是想用一种比较轻松、简单的方式说明其中的重点且常用的内容，在写作的过程中我也时常告诫自己要克制，别整复杂了。

Python 是一门很容易入门的语言，但是要进阶其实需要花费大量的时间和精力，而且还需要不断的练习使用，或许你已经花了两个月时间学习了 Python 基础并能够写一些小脚本，或许你已经达到一定高度能独立编写大型项目，但是学习永无止境，我们都还有很多需要学习提升的地方。以下内容绝大部分都是我在项目中用过的，很多描述是我自己的理解，可能会和官方有一定出入，但是相信大差不差，也欢迎有心人不吝赐教。

内容还会继续增加，包括一些简单好用的标准库、三方库都会持续加进来，希望看到的同学可以多多提意见。

## 二、类和对象

### 1、鸭子类型

“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。” 这是百科上对它的解释。

鸭子类型（duck typing）是动态类型的一种风格，鸭子类型对于 Python 编码来讲非常重要，理解它能让你真正理解什么是一切皆对象，更有助于我们理解这门语言的设计思想和实现原理，而不是仅仅浮于表面的念经 “一切皆对象”。

鸭子类型始终贯穿于 Python 代码当中，一个对象它是什么类型取决于它实现了什么协议，因此可以说 Python 是一种基于协议的编程语言。

那这些协议是什么，又有哪些协议？这里的协议，更多的时候我们称为魔法函数或魔法方法，因为它具有很多神奇的魔力，坊间因此称之为魔法函数。

在 Python 里面，所有以双下划线开头，且以双下划线结尾的函数都是魔法函数，就像 `__init__` 这种，它们是 Python 语言天然自带的，不是通过某个类去继承而来的，我们也不要随意去自定义一个这样的函数，小心着魔。

魔法函数有很多，但是经常用到的也没多少，常用的一些魔法函数在后面的内容会逐步介绍到。

### 2、类型判断

在判断数据类型的时候常见的有两种方法：`isinstance` 和 `type` 

```python
isinstance("123", str)  # 返回布尔值
type("123")  # 直接返回类型
```

isinstance 主要用于判断对象的类型。这个好理解，不多讲。

type 可以查看类型，但它能做的远不止于此，它主要用于动态的创建类。

```python
t = type("Mikigo", (), {"name": "huangmingqiang"})
T = t()
print(t)
print(T.name)
print(type(t))
```

```python
<class '__main__.Mikigo'>
huangmingqiang
<class 'type'>
```

你看，我们定义了一个类并赋值给 t，类名为 `Mikigo`，t 是类对象的引用，name 是其中的属性，Python 中一切都是对象，类也是对象，只不过是一种特殊的对象，是 `type` 的对象。

这个地方有点绕哈，你细品。

我看到网上好多讲 `type` 函数，准确讲 `type` 是一个类，只是用法像函数。在源码中：（通过 `Pycharm` 按住 `Ctrl` 点击进入）

```python
class type(object):

    def __init__(cls, what, bases=None, dict=None): # known special case of type.__init__
        """
        type(object_or_name, bases, dict)
        type(object) -> the object's type
        type(name, bases, dict) -> a new type
        # (copied from class doc)
        """
        pass
```

有同学要问了，为什么源码里面有 `pass`，你没看错，源码里面就是写的 `pass`，这种实际上是由于底层是由 C 语言实现的（本文内容都是基于 `CPython`），一般的操作是看不到源码的，之所以能看到是因为 `Pycharm` 给我们提供的功能（其他编辑器不知道哈，没咋用过其他的），相当于以代码的形式看文档，所以我们看到的不是真正的源码，但是最接近于源码的源码，姑且称之为源码吧。

type 的参数说明：

- 当 type() 只有一个参数时，其作用就是返回变量或对象的类型。

- 当 type() 有三个参数时，其作用就是创建类对象：
  
  - 参数 1：`what` 表示类名称，字符串类型；
  - 参数 2：`bases` 表示继承对象（父类），元组类型，单元素使用逗号；
  - 参数 3：`dict` 表示属性，这里可以填写类属性、类方式、静态方法，采用字典格式，`key` 为属性名，`value` 为属性值。
  
  ```python
  @staticmethod
  def my_static():
      print("this is static")
  
  t = type("Mikigo", (), {"name": "huangmingqiang", "static": my_static})
  T = t()
  t.static()
  T.static()
  ```
  
  ```python
  this is static
  this is static
  ```
  
  这样就添加了一个静态方法，很清楚哈，关于静态方法是什么我们后面会讲到，这里只需要知道 type 创建类的方法就好了。

通过上面 type 的源码可以看到，type 是继承了 object 的，我们知道所有类的顶层类都是继承的 object，那 object 又是从哪里来的？打印看一下：

```python
print(type(object))
```

```python
<class 'type'>
```

好家伙，object 也是由 type 创建的，前面说了 type 继承了 object，这俩哥们儿完美闭环了，我直接好家伙，理解起来有点更绕了哈。

你也可以说 type 自己创建了自己，这里要细细的品。实际上如果你了解指针的概念，这里其实也不难理解，不就是自己指向自己嘛，所以说 type 创建了所有类，因为他连他自己都不放过，还有什么事情做不出来。

### 3、类变量和实例变量

（1）类变量是在类里面直接定义的变量，它可以被类对象访问和赋值，也可以被实例对象访问和赋值。

```python
class Test:
    b = 1

    def __init__(self):  # 构造函数
        self.a = 1

T = Test()
print(T.b)
print(Test.b)
T.b = 2  # 通过实例对象赋值
print(T.b)
Test.b = 2 # 通过类对象赋值
print(Test.b)
```

```python
1
1
2
2
```

b 是类变量，都能被访问和赋值，没问题哈。

（2）实例变量是在构造函数里面定义的变量，它可以被实例对象访问和赋值，不能被类对象访问和赋值。

```python
class Test:
    b = 1

    def __init__(self):
        self.a = 1

T = Test()
print(T.a)
T.a = 2
print(T.a)
print(Test.a)
Test.a = 2
print(Test.a)
```

```python
1
2
Traceback (most recent call last):
  File "/tmp/pycharm_project_16/123.py", line 12, in <module>
    print(Test.a)
AttributeError: type object 'Test' has no attribute 'a'
```

a 是实例变量，你看实例对象访问和赋值正常的，类对象访问就报错了。

### 4、类方法、静态方法和实例方法

（1）实例方法又称对象方法，是类中最常见的一种方法。

```python
class Test:
    
    def obj_method(self):
        print("this is obj method")
```

实例方法参数必须传入 `self` ，`self` 表示实例对象本身，实例方法的调用也必须通过实例对象来调用：

```python
Test().obj_method()
```

（2）类方法

```python
class Test:
    
    @classmethod
    def cls_method(cls):
        print("this is class method")
```

可以通过类对象调用，也可以通过实例对象调用。

```python
Test.cls_method()
Test().cls_method()
```

注意两点：

- 方法前面必须加装饰器 `classmethod` ，装饰器是 `Python` 中的一种语法糖，后面会讲到，记住这种固定用法，这种写法也是初代装饰器的用法。
- 参数传入 `cls` ，`cls` 表示类对象，但是注意不是必须的写法，写 `cls` 是一种约定俗成的写法，方便我们理解，也就是说这里你写 `self` 从语法上也是不会有问题的。这就是为什么有时候我们将一个实例方法改成类方法，直接在方法前面添加了装饰器，而没有改 `self`，仍然能正常执行的原因。

（3）静态方法，实际上就是普通的函数，和这个类没有任何关系，它只是进入类的名称空间。

```python
class Test:
    
    @staticmethod
    def static_method():
        print("this is static method")
```

不需要传入任何参数。同样，可以通过类对象调用，也可以通过实例对象调用。

```python
Test.static_method()
Test().static_method()
```

我看到一些社区大佬都表现出对静态方法的嫌弃，他们觉得既然静态方法和类没有关系，何不如在类外面写，直接写在模块里面岂不快哉。咱们不予评价，存在即合理。

### 5、类和实例属性的查找顺序

这里需要引入一个概念：`MRO（Method Resolution Order）`，直译过来就是“方法查找顺序”。

大家知道类是可以继承的，子类继承了父类，子类就可以调用父类的属性和方法，那么在多继承的情况下，子类在调用父类方法时的逻辑时怎样的呢，如果多个父类中存在相同的方法，调用逻辑又是怎样的呢，这就是 `MRO`。

在` Python2.3` 之前的一些查找算法，比如：深度优先（`deep first search`）、广度优化等，对于一些菱形继承的问题都不能很好的处理。这部分内容比较多且杂，可以自己查阅资料。

在 `Python2.3` 之后，方法的查找算法都统一为叫 `C3` 的查找算法，升级之后的算法更加复杂，采用的特技版拓扑排序，这里也不细讲，可以自己查阅资料，我们只需要关心现在方法查找顺序是怎样的就行了。

来，这里举例说明：

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(C.__mro__)
```

`__mro__` 可以查看方法的查找顺序。

```python
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

可以看到，对于 C 来讲，它里面的方法查找顺序是 C — A — B，没毛病哈，很清楚。

现在升级一下继承关系，试试菱形继承：

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)
```

```python
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

D 的查找顺序是 D — B — C — A

说明什么问题？我在这噼里啪啦说了这么多，到底想说啥？

想象一下，如果你在 B 和 C 里面都重载了 A 里面的一个方法，此时如果你想调用的是 C 里面的方法，实际上是无法调用的，因为根据方法的查找顺序，会先找到 B 里面的方法。

因此，重点来了：在 Python 中虽然是支持多继承的，但是在实际项目中不建议使用多继承，因为如果继承关系设计得不好，很容易造成逻辑关系的混乱，原因就是 `MRO`。

Ruby 之父在《松本行弘的程序世界》书中，讲到三点多继承的问题：

>- 结构复杂化：如果是单一继承，一个类的父类是什么，父类的父类是什么，都很明确，因为只有单一的继承关系，然而如果是多重继承的话，一个类有多个父类，这些父类又有自己的父类，那么类之间的关系就很复杂了。

>- 优先顺序模糊：假如我有A，C类同时继承了基类，B类继承了A类，然后D类又同时继承了B和C类，所以D类继承父类的方法的顺序应该是D、B、A、C还是D、B、C、A，或者是其他的顺序，很不明确。

>- 功能冲突：因为多重继承有多个父类，所以当不同的父类中有相同的方法是就会产生冲突。如果B类和C类同时又有相同的方法时，D继承的是哪个方法就不明确了，因为存在两种可能性。

看看这是大佬说的，不是我说的。

那有同学要问了，我写的功能很复杂啊，必须要继承多个类，怎么办，难受！

实际上有一种比较流行且先进的设计模式：`Mixin` 混合模式，完美解决这个问题。

举个简单的例子：

```python
class Animal:
    pass

# 大类
class Mammal(Animal):
    pass

# 各种动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass
```

现在动物们没有任何技能，咱们需要给动物们增加一下技能：

```python
class RunnableMixIn:
    def run(self):
        print('Running...')

class FlyableMixIn:
    def fly(self):
        print('Flying...')
```

注意 `Mixin` 的类功能是独立的，命名上也应该使用 `MixIn` 结尾，这是一种规范。

需要 Run 技能的动物：

```python
class Dog(Mammal, RunnableMixIn):
    pass
```

需要 Fly 技能的动物：

```python
class Bat(Mammal, FlyableMixIn):
    pass
```

有点感觉了没，`Mixin` 类的特点：

- 功能独立、单一；
- 只用于拓展子类的功能，不能影响子类的主要功能，子类也不能依赖 `Mixin`；
- 自身不应该进行实例化，仅用于被子类继承。

`Mixin` 设计思想简单讲就是：不与任何类关联，可与任何类组合。

### 6、破解私有属性

私有属性就是在类的内部能访问，外部不能访问。

在 Python 中没有专门的语句进行私有化，而通过在属性或方法前面加“两个下划线”实现。

举例：

```python
class Test:

    def __init__(self):
        self.__mi = "Mikigo" 

    def __ki(self):
        print("Mikigo")
        
    def go(self):
        print(self.__mi)
```

```python
Test().go()
```

```python
Mikigo
```

你看，在类的内部访问私有属性是可以正常拿到的，方法也是一样的。

现在我们访问私有属性试试：

```python
Test().__mi
```

```python
Traceback (most recent call last):
  File "/tmp/pycharm_project_609/123.py", line 6, in <module>
    print(Test().__mi)
AttributeError: 'Test' object has no attribute '__mi'
```

从外部进行私有属性访问是不行的，人家是私有的。

```python
Test().__ki()
```

```python
Traceback (most recent call last):
  File "/tmp/pycharm_project_609/123.py", line 9, in <module>
    Test().__ki()
AttributeError: 'Test' object has no attribute '__ki'
```

私有方法也无法访问，没问题哈。

有同学要问了，我就是想访问，越是私有的我越想看，怎么才能看到别人的隐私，快说！

泄露天机了哈，这是 Python 一种很奇妙的结构化处理，为什么说是结构化处理，实际上 Python 拿到双下划线之后，对其进行了变形，在前面加了一个下划线和类名，我们通过这种方式可以访问：

```python
print(Test()._Test__mi)
Test()._Test__ki()
```

```python
Mikigo
Mikigo
```

你看，这样就可以正常访问了，但是既然作者不希望使用者调用这个方法，我们也尽量不要去强行使用它，强扭的瓜不甜。

所以说，从语言的角度是没有绝对的安全，任何语言都是这样，更多的是一种编程上的约束。

通常在大多数实践中，我们更倾向于使用一个下划线来表示私有属性，这不是真正的私有，而是一种更友好的编程规范，社区称之为 “受保护的”属性，它向使用着表达了这是一个私有的方法，但是你仍然可以使用它，这就是社区，这就是开源，respect~。

### 7、对象的自省机制

自省(introspection)，即自我反省，而对象的自省实际上就是查看对象实现了哪些属性或方法。

简单讲就是，告诉别人：**我是谁，我能干啥**。

Python 的常用的自省函数有四个：dir()、type()、 hasattr()、isinstance()

（1）isinstance() 和 type() 前面也提到过，这里不讲了。

（2）dir() 是最为常用的一个自省函数：

引用前面的 Test 类

```python
print(dir(Test))
```

```python
['_Test__ki', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'go']
```

除了 `_Test__ki` 和 `go` 方法以外，其他的方法都是魔法函数，即最开始我们提到的协议，你看随便一个对象就实现了这么多协议，是不是很神奇。

（3）hasattr() 主要用于判断对象中是否包含某个属性，返回布尔值。

```python
print(hasattr(Test, "go"))
print(hasattr(Test, "wo"))
```

```python
True
False
```

很简单，不多讲哈。

其他还有一些自省函数可以了解一下，偶尔用到也挺好的：

- `__doc__` 获取到文档字符串；
- `__name__` 获取对象的名称；
- `__dict__` 包含了类里可用的属性名-属性的字典；
- `__bases__` 返回父类对象的元组；但不包含继承树更上层的其他类。

### 8、super

super 函数是用于调用父类的一个方法。

```python
class A:

    def mi(self):
        print("=== mi ===")

class B(A):

    def ki(self):
        super().mi()
```

```python
B().ki()
```

```python
=== mi ===
```

super 的使用方法是很简单的，但是如果涉及到多继承的情况下，就要小心处理。

准确的讲它不是调用父类的方法，而是调用的 `MRO` 顺序上的下一个方法。

### 9、上下文管理器

在讲到上下文管理器的时候，经常有同学一脸懵，然后我说 `with` 的时候，就会脱口而出 `with open` 。

没错，with 语句用得最多的也是这个，它是 Python 提供的一种处理资源回收的神奇方法，如果没有 with 我们可能需要多写很多代码。

大家都知道打开一个文件之后是需要关闭的，但是在操作文件的过程中很容易报错，这时候我们需要进行异常处理，要保证无论是否存在异常的情况下，文件都能正常的被关闭，我们几乎只能使用try里面的finally来处理：

```python
f = open("test.txt", "w")
try:
    f.write(some_txt)
except:
    pass
finally:
    f.close()
```

如果用 with 语句处理就会很简单：

```python
with open("test.txt", "w") as f:
    f.write(some_txt)
```

对比起来，哪个更好不用多说，自己品。

在《流畅的 Python》这本书里面提到：

>  在任何情况下，包括CPython，最好显式关闭文件；而关闭文件的最可靠方式是使用with语句，它能保证文件一定会被关闭，即使打开文件时抛出了异常也无妨。

那我们如何实现一个上下文管理器呢？

- **基于类实现上下文管理器**

要实现上下文管理器，需要实现两个魔法函数：`__enter__` 和 `__exit__` 。

看名称就知道了，enter 就是进入的时候要做的事情，exit 就是退出的时候要做的事情，很好记有没有。

```python
class Context:

    def __init__(self, file_name):
        self.file_name = file_name
        self.f = None

    def __enter__(self):
        print("进入 with")
        self.f = open(self.file_name, "r")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出 with")
        if self.f:
            self.f.close()
```

然后我们就可以使用 with 语句

```python
with Context("test.txt") as f:
    print(f.read())
```

```python
进入 with
我是一个测试文件
退出 with
```

完美哈，一个上下文管理器的类就轻松搞定。

- **基于 contextlib 实现上下文管理器**

还有种通过标准库实现上下文管理器的方法：

```python
from contextlib import contextmanager

@contextmanager
def context_test(file_name):
    print("进入 with")
    try:
        f = open(file_name, "r")
        yield f
    finally:
        print("退出 with")
        f.close()
```

来用 with 玩耍一下

```python
with context_test("test.txt") as f:
    print(f.read())
```

```python
进入 with
我是一个测试文件
退出 with
```

利用生成器的原理，yield 之前是进入，yield 之后是退出，同样可以实现一个上下文管理器，稍微理解一下哈。

上下文管理器是 Python 提供给我们的一个非常方便且有趣的功能，经常被用在打开文件、数据库连接、网络连接、摄像头连接等场景下。如果你经常做一些固定的开始和结尾的动作，可以尝试一下。

### 10、装饰器

装饰器就是使用 @ 符号，像帽子一样扣在函数的头上，是 Python 中的一种语法糖。

前面讲类方法和静态方法的时候提到过，使用方法非常简单。

原理实际上就是将它所装饰的函数作为参数，最后返回这个函数。

```python
@classmethod
def mikigo():
    print("My name is mikigo")
```

这样的写法等同于

```python
def mikigo():
    print("My name is mikigo")
    
mikigo = classmethod(mikigo)
```

对比一下，使用装饰器可读性很高，很优雅是吧，语法糖就是给你点糖吃，让你上瘾。

**定义一个装饰器**

- **不带参数的装饰器**

举个例子：

```python
def logger(func):
    def wrapper(*args, **kw):
        print('我要开始搞 {} 函数了'.format(func.__name__))
        func(*args, **kw)  # 函数执行
        print('搞完了')
    return wrapper
```

这是一个简单的装饰函数，用途就是在函数执行前后分别打印点日志。

有2点需要注意：

（1）装机器是一种高阶函数，在函数内层定义函数，并返回内层函数对象，多层级同理。

（2）最外层函数传入的参数是被装饰函数的函数对象。

```python
@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))
```

来，试试看

```python
add(5, 10)
```

```console
我要开始搞 add 函数了
5 + 10 = 15
搞完了
```

- **带参数的装饰器**

```python
from functools import wraps

def logger(say_some):
    @wraps
    def wrapper(func):
        def deco(*args, **kw):
            print("搞之前我先说两句：{}".format(say_some))
            print('我要开始搞 {} 函数了:'.format(func.__name__))
            func(*args, **kw)  # 函数执行
            print('搞完了')
        return deco
    return wrapper
```

你看，都是外层函数返回内层函数对象，参数放在最外层。`@wraps` 可加可不加，它的用途主要是保留被装饰函数的一些属性值。

```python
@logger("别整，不得劲儿~")
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))
```

执行试试

```python
add(5, 10)
```

```console
搞之前我先说两句：别整，不得劲儿~
我要开始搞 add 函数了:
5 + 10 = 15
搞完了
```

很奈斯，就这点儿东西。

这是最常见的实现方法，现在咱们搞点不一样的。

**基于类实现装饰器**

基于类装饰器的实现，必须实现 `__call__` 和 `__init__` 两个魔法函数。

- **不带参数的类装饰器**

```python
class logger:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('我要开始搞 {} 函数了'.format(self.func.__name__))
        f = self.func(*args, **kwargs)
        print('搞完了')
        return f
```

不带参数的类装饰，func 是通过 init 函数里面构造的。

试试看

```python
@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))
```

```python
add(5, 10)
```

```python
我要开始搞 add 函数了
5 + 10 = 15
搞完了
```

so easy 哈，鸭子类型，实现了装饰器协议，就是装饰器对象。

- **带参数的类装饰器**

```python
class logger:

    def __init__(self, say_some):
        self.say_some = say_some

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("搞之前我先说两句：{}".format(self.say_some))
            print('我要开始搞 {} 函数了'.format(func.__name__))
            func(*args, **kwargs)
            print('搞完了')
        return wrapper
```

带参数的类装饰器，func 是在 call 函数里面，参数是通过 init函数传入的，这里区别比较大哈。

```python
@logger("别整，真的不得劲儿~")
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))
```

```python
add(5, 10)
```

```console
搞之前我先说两句：别整，真的不得劲儿~
我要开始搞 add 函数了
5 + 10 = 15
搞完了
```

这类属于装饰器的高阶用法了，在一些优秀的框架源码里面比较常见。

## 三、自定义序列

### 1、可切片对象

切片大家都很熟悉，在 Python 基础里面是必学的，对列表使用中括号取值，正切、反切、加步长等都没问题，这里我们主要讲怎么实现一个可切片对象。

隆重请出魔法函数：`__getitem__` ，它是我们实现可切片对象的关键。

```python
class AutoTest:

    def __init__(self, name_list):
        self.name_list = name_list

    def __getitem__(self, item):
        return self.name_list[item]
    
AT = AutoTest(["mikigo", "lt", "jjb", "hhz"])
```

咱们对实例对象切片试试

```python
print(AT[1])
print(AT[2])
```

```console
lt
jjb
```

简直没难度哈，对象可以切片了。

这里再补充一点没有用的小知识，实现了 `__getitem__` 方法实际上也是一个可迭代的对象了，也就是说可以使用 for 循环。

```python
for i in AT:
    print(i)
```

```console
mikigo
lt
jjb
hhz
```

这其实是可迭代对象的一种退而求其次的处理，它找不到迭代协议，但是找到了 `__getitem__` ，也可以进行迭代，这点相信 99% 的同学都不知道，没关系哈，关于可迭代对象和迭代器咱们后面会专门讲。

### 2、列表推导式

列表推导是 Python 提供的一种独有特性，可以用一行代码生成一个列表。

普通操作：

```
my_list = []
for i in range(10):
    my_list.append(i)
```

这样生成一个列表，至少需要3行，来看看列表推导式：

```python
my_list = [i for i in rang(10)]
```

一行就搞定，多么的简洁优雅，而且可读性和性能都非常高，爱了。

还可以加一些逻辑判断和数据处理，以下是项目实例：

```python
app_id_list = [int(_id) for _id in app_id if _id]  # to int
```

这里要提醒一下，不要为了推导而推导，如果你的逻辑很复杂，加了多重判断和处理，不建议使用推导式，老老实实分开写，因为这样写出来的表达式会很复杂，就失去了我们编码最重要的一点，就是可读性。

### 3、生成器表达式

前面讲了列表推导式，是用中括号里面写表达式，那把中括号换成小括号是什么呢？好多同学聪明的小脑袋肯定想到了，元组推导式 ... 。

注意元组是不可变序列，没法推导的，小括号的表达式实际上是生成器表达式。

```python
my_gen = (i for i in range(10))
```

验证一下：

```python
from collections.abc import Generator

print(isinstance(my_gen, Generator))
print(my_gen)
```

```console
True
<generator object <genexpr> at 0x7f5676c57390>
```

你看，确实是一个生成器吧。生成器细节，咱们也放到后面讲哈。

### 4、字典推导式

理解了列表推导式，再来看字典推导式就很简单了。

```python
my_dict = {i: None for i in range(10)}
```

第一个元素就是字典的 key 和 value，注意字典的key 是唯一的（可哈希），值无所谓。

打印看下

```python
print(my_dict)
```

```console
{0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
```

就这，简直没难度，还是要注意一点，代码可读性哈，别整复杂了。

```python
tag_dict = {f"{int(i[0]):0>3}": i[1:] for i in ReadCsv.read_csv_by_str(csv_dict.get(app), from_data=False)}
```

这是自动化测试项目中的一个实例，感受下，如果再复杂点就建议拆开写了。

## 四、对象引用

### 1、变量到底是什么

在 Python 中变量到底是什么，有一个比喻我觉得非常好，变量就像便利贴。

为什么这么讲，我们定义一个数据，比如定义一个字符串或者整数，在内存中都会分配一个空间来保存，这个内存空间相当于一个小盒子，我们使用等号将这个数据赋值给一个变量时，实际上就像用便利贴贴到这个小盒子上，便利贴上还写了名称，就是变量名。所以说，变量和数据的关系只是一个指向的关系。

一个数据可以赋值给多个变量，相当于这个小盒子上面贴了多个便利贴；一个变量也可以被重新赋值，相当于把这个盒子上的便利贴撕了，贴到另一个盒子上。

变量和数据的关系，就是盒子和便利贴的关系，理解起来很容易。

函数名也是变量，是可以传参的变量，也同样是便利贴。

### 2、== 和 is 是一样的吗

这两个在编程中经常用到，好多同学经常搞不清楚应该用哪个。

- == 是比较两边的“值”是否相等;
- is 是判断是否为同一个对象，即 id 是否一样。

```python
a = 1000
b = 1000

print(a == b)
print(a is b)
print(id(a), id(b))
```

```console
True
True
140689217239312 140689217239312
```

这里有个很神奇的地方，分别定义了两个变量a, b，他们的值相等，但是这样定义应该是分配了2个内存空间，更有意思的是，如果你通过命令行执行以上代码，结果会不一样：

有这个符号的 `>>>` 表示是在命令行执行。

```console
>>> a = 1000
>>> b = 1000
>>> print(a == b)
True
>>> print(a is b)
False
>>> print(id(a), id(b))
140601647494256 140601647494448
```

上面是使用 `Pycharm` 执行的，实际上Python解释器已经对经常使用到的小整数做了特殊处理，解释器会提前将 256 以内的整数申请内存空间，不会回收，以提升执行效率，所以在这个范围内的整数 id 永远是一样的。

```console
>>> a = 256
>>> b = 256
>>> print(id(a), id(b))
9095360 9095360
```

```console
>>> a = 257
>>> b = 257
>>> print(id(a), id(b))
140601647494512 140601647494384
```

`Pycharm` 在解释器的基础之上做了进一步的优化。

```python
a = 1000000
b = 1000000

print(id(a), id(b))
140061167311120 140061167311120
```

你看，这么大的数字 id 也是相同的，`Pycharm` 就是这么酷。

### 3、del语句和垃圾回收

在 Python 中的垃圾回收机制是：引用计数（Reference Counting）。

简单讲就是每个对象内部有一个引用计数器，对象被创建或者被引用就会 +1，对象被销毁或者被赋予新的对象就会 -1

del 语句是作用在变量上，不是数据对象上。

```python
a = 1
b = a
del a
```

打印 b 看下

```python
print(b)
```

```console
1
```

再打印 a 看下

```python
print(a)
```

```python
NameError: name 'a' is not defined
```

很明显，a 被删掉了。

之前看到国外的一个大佬讲 open 的这种写法不用关闭：

```python
open("test.txt", "r").read()
```

很有意思是吧，这点没有用的小知识，相信你在网上应该查不到。当时觉得不太理解，后面理解垃圾回收之后才明白，使用 open 打开的文件对象创建之后，没有被其他引用，所以会被内存回收的，因而不用关闭也不影响。

邪门歪道哈，用 open 还是老老实实用 with 吧。

## 五、元类编程

### 1、动态属性和属性描述符

有些同学可能知道 `@property` ，它的主要用于将一个方法变成属性，访问的时候直接通过名称访问，不需要加括号。注意加了 `@property` 函数不能有参数，你想嘛，人家调用的时候都不用括号，怎么传参，对吧。

举个小例子：

```python
class Mikigo:

    @property
    def age(self):
        return "我晕，今年30了"

print(Mikigo().age)
```

```console
我晕，今年30了
```

你看，调用 age 方法没加括号吧，那我要修改 age 的值怎么做呢？

```python
class Mikigo:

    def __init__(self):
        self._age = 30

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError
        self._age = value

mi = Mikigo()
mi.age = 25
print(mi.age)
```

```console
25
```

注意上例中装饰器的写法，setter 是固定写法，setter 前面是你定义的函数名。

没什么问题哈，做了参数的类型检查，整体看起来不算复杂，其实了解到这里已经差不多了。但是，如果我们还有其他属性要处理，就得写好多个这样的，挺费劲不说，关键是不够优雅。

这时候就需要请出属性描述符。

这里又要介绍两个魔法函数：`__get__`， `__set__`。

举个例子，讲解其用法：

```python
class UserAttr:

    def __init__(self, user_age):
        self._age = user_age

    def __get__(self, instance, owner):
        print("get_instance:", instance)
        print("get_owner:", owner)
        return self._age

    def __set__(self, instance, value):
        print("set_instance:", instance)
        print("gse_value:", value)
        if not isinstance(value, int):
            raise ValueError
        self._age = value

```

真正使用的类：

```python
class Mikigo:
    age = UserAttr(30)

mi = Mikigo()
print(mi.age)
```

```console
get_instance: <__main__.Mikigo object at 0x7fb4eff50e10>
get_owner: <class '__main__.Mikigo'>
30
```

在对象访问 age 的时候，首先是进入了 `__get__` 方法，因为先打印了 get_instance 和 get_owner，instance 是 Mikigo 实例对象，也就是 mi，owner 是 Mikigo 类对象。

因此，到这里，我们知道了第一个小知识，在访问值的时候，调用的是 `__get__` 。

再赋值看看：

```python
mi.age = 25
print(mi.age)
```

```console
set_instance: <__main__.Mikigo object at 0x7fc7be222470>
set_value: 25
get_instance: <__main__.Mikigo object at 0x7fc7be222470>
get_owner: <class '__main__.Mikigo'>
25
```

第二个小知识，赋值是调用的 `__set__` 方法，一般为了使属性描述符成为只读的，应该同时定义 `__get__()` 和 `__set__()` ，并在 `__set__()` 中引发 `AttributeError` 。

还有一个魔法函数 `__delete__` 也是属性描述符，使用 del 会调用，由于不咋使用，不讲了，还有网上好多区分数据描述符和非数据描述符的，我感觉不用管也没必要，咱们是通俗易懂版，不整那些。

### 2、属性拦截器

属性拦截器就是在访问对象的属性时要做的一些事情，你想嘛，拦截就是拦路抢劫，拦截下来肯定要搞点事情才放你走。

主要介绍 2 个魔法函数：`__getattr__` 和 `__getattribute__`

这两个函数特别神奇，两个函数功能相反，一个是找到属性要做的事，另一个是没找到属性要做的事。

```python
class Mikigo:

    def __init__(self):
        self.age = 30

    def __getattribute__(self, item):
        print(f"找到{item}，我先搞点事情")

    def __getattr__(self, item):
        print(f"没找到{item}，我想想能搞点啥事情")
```

定义了一个属性 age ，先来试试访问它

```python
mi = Mikigo()
print(mi.age)
```

```console
找到age，我先搞点事情
30
```

找到属性，会先调用 `__getattribute__` ，并没有调用 `__getattr__`。

好，现在访问一个不存在的属性：

```python
mi.name
```

```console
找到name，我先搞点事情
没找到name，我想想能搞点啥事情
```

这里就需要注意了，访问一个不存在的属性，首先还是会进入 `__getattribute__` ，说明它是无条件进入的，然后才是调用 `__getattr__`。

再扩展一个 `__setattr__` 用于修改属性值的：

```python
class Mikigo:
    def __init__(self):
        self.age = 30

    def __setattr__(self, key, value):
        print(f"修改{key}的值为{value}")
        self.__dict__[key] = value

mi = Mikigo()
mi.age = 25
print(mi.age)
```

```python
修改age的值为30
修改age的值为25
25
```

你看，age 的值被修改了，但是 `__setattr__` 貌似被调用了 2 次，那是因为在类实例化的时候就会进入一次，第一次是将 `__init__` 里面的值添加到类实例的 `__dict__` 属性中，第二次修改再次进入，将 `__dict__` 属性中的值修改掉。

属性拦截一定要谨慎使用，一般情况下不建议使用，因为如果处理不好，会造成类里面属性关系的混乱，抛异常往往不容易定位。

项目实例，config 文件里面用到：

```python
class Config:
    default = {
        # for cases
        "SMB_URL": "SMB://10.8.10.214",
        "SMB_IP": "10.8.10.214",
    }

    def __getattr__(self, key):
        try:
            return Config.default[key]
        except KeyError:
            raise AttributeError(f"{key} is not a valid option!") from KeyError

    def __setattr__(self, key, value):
        if key not in Config.default:
            raise AttributeError(f"{key} is not a valid option!") from KeyError
        Config.default[key] = value
```

试着分析下他们的作用吧，逻辑很简单的，你一定能看懂。

### 3、自定义元类

元类（metaclass）就是生成类的类，先定义metaclass，就可以创建类，最后创建实例。

其实最开始讲 type 的时候已经有所接触了，type 生成了所有类，它就是顶层元类，metaclass 也是要继承 type的，排行顶多老二，是不是应该叫“元二类”，或者“元类二”，爱谁谁吧。

来，咱们定义一个元类，用途是添加一个属性 age ：

```python
class AutoTestMetaClass(type):

    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.age = 30
        return x

```

这里有 2 个知识点：

- `__new__` 也是构造函数，和 `__init__` 有区别，`__new__` 是用来构造类对象的，你看它的参数是 cls，必须 return 一个对象。
- name, bases, dct 这三个参数和 type 的三个参数是一个意思，不清楚可以回看前面讲 type 的章节。

元类有了，咱们使用一下，既然元类是用来生成类的类，那咱们就来生成一个类：

```python
class Mikigo(metaclass=AutoTestMetaClass):
    ...

mi = Mikigo()
print(mi.age)
print(Mikigo.age)
```

```console
30
30
```

咱们定义一个类除了省略号没有任何属性，省略号也是一个对象，你也可以用 pass，但是仍然可以访问 age 属性。因为我们是通过元类，向 Mikigo 这个类添加了一个属性，元类有时称为类工厂。

## 六、迭代器和生成器

### 1、迭代协议

迭代就是可以使用循环将数据挨个挨个取出来，这个好理解是吧，比如，咱们常见的对一个列表进行迭代：

```python
for i in [1, 2, 3]:
    print(i)
```

结果不用讲肯定是挨着取出列表里面的数字了。

那列表里面究竟是实现了什么协议，或者说一个对象实现什么魔法函数就可以迭代呢，这就是迭代协议：`__iter__`

一个类只要实现了魔法函数 `__iter__` 就是可迭代的（`Iterable`），但是它还不是迭代器(`Iterator`)，品一下区别。

```python
class IterTest:

    def __iter__(self):
        ...
```

来验证一下：

```python
from collections.abc import Iterable
from collections.abc import Iterator

print("是否可迭代：", isinstance(IterTest(), Iterable))
print("是否为迭代器：", isinstance(IterTest(), Iterator))
```

```console
是否可迭代：True
是否为迭代器：False
```

你看实现了迭代协议，就是可迭代的，想起鸭子类型了吗。

### 2、迭代器和可迭代对象

我们现在知道一个对象只要实现了 `__iter__` 就是一个可迭代的对象，现在咱们来试试对一个可迭代对象使用 for 循环进行迭代，放个简单的列表进去看看：

```python
class IterTest:

    def __iter__(self):
        return [1, 2, 3]

for i in IterTest():
    print(i)
```

在 `__iter__` 函数里面返回一个列表，列表是一个可迭代的对象，但不是迭代器。

```python
Traceback (most recent call last):
  File "/tmp/pycharm_project_609/123.py", line 11, in <module>
    for i in IterTest():
TypeError: iter() returned non-iterator of type 'list'
```

运行报错了，说 iter 返回了一个不是迭代器的对象。说明在 `__iter__` 里面需要返回一个迭代器，对吧，其他的先不管，咱们放一个迭代器进去，保证程序跑起来不报错。

放一个生成器表达式进去试试：

```python
class IterTest:

    def __iter__(self):
        return (i for i in range(3))

for i in IterTest():
    print(i)
```

```console
0
1
2
```

唉，这下对了，没报错，而且也能迭代出来了。

但是，此时仍然还不是一个迭代器，要实现迭代器，还必须要实现另外一个魔法函数：`__next__`

```python
class IterTest:

    def __iter__(self):
        return (i for i in range(3))

    def __next__(self):
        ...
```

验证一下

```python
print("是否为迭代器：", isinstance(IterTest(), Iterator))
```

```console
是否为迭代器： True
```

你看，实现 `__next__` 之后，就是一个迭代器了。那 `__next__` 应该怎么写，前面我们已经看到， `__iter__` 里面是不负责逻辑处理的，它只管返回，逻辑处理需要在 `__next__` 里面去做。

使用经典的斐波那契数列来举例：

```python
class Fib:
    def __init__(self, n):
        self.a, self.b = 0, 1
        self.n = n

    # 返回迭代器对象本身
    def __iter__(self):
        return self

    # 返回容器下一个元素
    def __next__(self):
        if self.n > 0:
            self.a, self.b = self.b, self.a + self.b
            self.n -= 1
            return self.a
        else:
            raise StopIteration
```

这里面 n 是用来限制迭代次数的，不然这个循环将一直进行下去，直到宇宙的尽头，抛 `StopIteration` 异常会被 `for` 循环自动处理掉。

```python
for i in Fib(10):
    print(i)
```

```console
1
2
3
5
8
13
21
34
55
```

这样我们就实现了一个简单的迭代器。

简单一句话总结一下：迭代器就是使对象可以进行 for 循环，它需要实现 `__iter__` 和 `__next__` 两个魔法函数。

有同学要说了，就这？不就用 for 循环嘛，搞这么复杂嘎哈，我为什么要用迭代器啊？

**为什么要使用迭代器**

节省资源消耗，迭代器并不会计算每一项的值，它只在你访问这些项的时候才计算，也就是说它保存的是一种计算方法，而不是计算的结果。能理解吗，相当于迭代器是鱼竿，而不是一池子的鱼，需要鱼的时候钓就行了，而不用把所有鱼都搬回家。

平时可能感受不到哈，当你需要计算一个非常大的数据时，你就能感受到了，这就是“惰性求值”的魅力。

你可以试试前面的斐波那契数列的列子，对比一个普通的列表，然后给一个很大的数字，区别就很明显了。

### 3、生成器

生成器也是一种迭代器，特殊的迭代器，它也可以用 for 循环来取值，但是大部分的情况下是使用 next() 函数进行取值。

前面我们讲生成器表达式已经见识过，这是一种便携的写生成器的方法：

```python
my_gen = (i for i in range(10))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
```

```console
0
1
2
3
```

一般这么玩的哈。

前面讲的好多对象都是在类里面定义的，而生成器对象就不是在类里面了，而是在函数里面定义，在一个函数里面只要出现了 `yield` 它就不是普通函数，而是一个生成器。

```python
def my_gen():
    print("setp 1")
    yield 1
    print("setp 2")
    yield 2

g = my_gen()
next(g)
next(g)
```

```console
step 1
step 2
```

`yield` 的用途是让函数暂停，并保存对象状态在内存中，下次再使用 `next` 调用同一个对象时，又开始从之前暂停的位置开始执行，直到运行到下一个 `yield` 又暂停，如果后面没有 `yield`了，则会抛 `StopIteration` 异常。

`yield` 和 `return` 都能返回数据，但是有区别，`return` 语句之后的代码是不执行的，而 `yield` 后面还可以执行。

有同学要问了，生成器函数里面能用 `return` 吗？好问题，不愧是你。

生成器里面是可以用 `return` 的，但是，`return` 后面的数据不会被返回。

举例：

```python
def my_gen():
    yield 1
    yield 2
    return 3

for i in my_gen():
    print(i)
```

```console
1
2
```

你看，3 并没有被返回，所以说生成器里面的 `return` 只是一个结束的标志，它不会把后面的值返回给调用者，这跟函数里面的 `return` 是不一样的。

### 4、总结

看完前面迭代器和生成器的内容，可能有些同学有点晕了，没关系，多看几遍，经常看，经常晕。

我们简单总结一下：

- 迭代器需要实现两个魔法函数：`__iter__` 和 `__next__` ；

- 迭代器允许惰性求值，只有在请求下一个元素时迭代器对象才会去生成它，它保存的是一种生成数据的方法；
- 生成器是迭代器的一种更 `Pythonic` 的写法，可以在函数里面用 `yield` 创建一个迭代器；
- 生成器表达式是生成器的一种更加 `Pythonic` 的写法。

## 七、高阶函数

高阶函数是通过组合简单函数成一个复杂表达式的函数。你可以理解成，函数套函数。函数式编程是一种编程范式，这部分内容可以体现 Python 在函数式编程上的应用。

### 1、lambda

匿名函数（lambda），这个函数没有函数名，用于一行创建一个函数，并返回一个函数对象，也是一种语法糖。

定义一个匿名函数，功能就是参数加1：

```python
my_lb = lambda x: x + 1
```

普通函数的写法就是：

```python
def add_one(n):
    return n + 1
```

你看，确实很简洁哈，my_lb 不是函数名哈，有函数名它就不是匿名函数了，而是函数对象，咱可以调用它。

```python
print(my_lb(1))
```

我个人觉得，匿名函数很尴尬，基本上都是用在下面几个高阶函数里面的，如果你平时也想用它，大多数情况下是不符合社区规范的。简单的表达式还行，复杂的表达式可读性太差。

传言 Python 之父 Guido 也不推荐使用它，甚至曾想过移除它，后来放弃了，估计是不好搞。就像 GIL 一样，大家都知道不好，但是这么多年下来太多库都用到了，哪是你想删就能删的，社区不答应，我也不答应。

### 2、map

map 函数是给一个序列做映射，然后返回结果序列。

简单通俗讲就是：拿到一个序列，给序列中元素一顿操作之后，返回序列。

```python
my_map = map(lambda x: x + 1, [1, 2, 3])
print(my_map)
my_list = list(my_map)
print(my_list)
```

```console
<map object at 0x7f201238cd68>
[2, 3, 4]
```

你看，map 返回的是一个对象，转 list 之后每个元素的加了1。

### 3、reduce

reduce 函数就是对一个序列做累积，即将序列中前一个元素和后一个元素进行逻辑组合，然后结果再和后面一个元素组合。

简单通俗讲就是：拿到一个或多个序列，给序列中元素一顿操作之后，返回操作结果。

```python
from functools import reduce

my_rd = reduce(lambda x, y: x + y, [1, 2, 3])
print(my_rd)
```

```console
6
```

你看，把列表中的元素都相加了，注意组合关系不一定是相加，你可以换成相乘试试。

乍一看和上面的 map 是一个意思哈，确实用法一样，区别就是 reduce 函数里面的 lambda 函数有**两个参数**，而 map 函数参数理论上可以多个，但是每个参数对应一个序列，也就是说，**有多少个参数，就要有多少个序列**。

### 4、filter

filter 函数用于过滤的，即将序列中的每个元素进行判断，然后返回为 True 的元素。

```python
my_ft = filter(lambda x: x % 2 == 1, [1, 2, 3])
print(my_ft)
my_list = list(my_ft)
print(my_list)
```

```python
<filter object at 0x7f778f58fd68>
[1, 3]
```

判断序列中哪些数是奇数，filter 返回的是一个对象，转列表之后，可以看到结果。

### 5、sorted

sorted 函数用于排序，好多同学可能用过它的参数 reverse=False 升序（默认），reverse=True 降序，但是还有个参数 key 可能没咋用过，这里可以给表达式。

```python
my_st = sorted([1, 5, 3])
print(my_st)
my_st = sorted([1, 5, 3], reverse=True)
print(my_st)
```

```console
[1, 3, 5]
[5, 3, 1]
```

数字排序还是挺好用的哈，处理简单的字符串也都可以，但是如果是处理比较复杂字符串排序就有点费劲了，不信试试看：

```python
test_list = ["test_mi_001","test_ki_012","test_go_008","test_lt_003"]
```

我想让这个列表按照结尾的序号排序：

```python
my_st = sorted(test_list)
print(my_st)
```

```console
['test_go_008', 'test_ki_012', 'test_lt_003', 'test_mi_001']
```

排了个寂寞，无论是升序还是降序都是不行的。

所以需要使用参数 key，加表达式：

```python
my_st = sorted(test_list, key=lambda x: x.split("_")[-1])
print(my_st)
```

```console
['test_mi_001', 'test_lt_003', 'test_go_008', 'test_ki_012']
```

唉，这就对了，我们在表达式里面将结尾的序号取出来，key 就是关键字，意思就是按照我取出来的关键字排序。这里稍微理解一下哈，里面的表达式比较灵活，你也可以用正则表达式来做：

```python
import re
my_st = sorted(test_list, key=lambda x: re.findall(r"\d+", x))
```

也都是可以的哈，没毛病。

它不仅可以对列表排序，只要是可迭代对象都可以，列表对象的内建方法 sort 也可以这样用，但区别是 sort 是对原列表进行排序，不返回新列表。

这里再补充一个小知识，我们经常往一个列表中去添加数据，然后对其进行排序，这样做没啥问题，但是如果数据量大了之后，性能会比较低。

维护一个排序序列，建议使用Python 的标准库 bisect 来做，它是采用二分查找算法，性能较高。

### 6、zip

zip 就是将多个序列打包成一个个元组，然后返回由这些元组组成的列表。

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)
print(c)
my_list = list(c)
print(my_list)
```

```console
<zip object at 0x7f4ada0fa548>
[(1, 4), (2, 5), (3, 6)]
```

zip 返回的是一个对象，实际上是一个迭代器对象。

转列表之后，可以看到，相当于是把元素纵向分别取出来，放到一个元组里面，然后元组组成一个列表。做数据处理的时候经常用到，了解一下。
