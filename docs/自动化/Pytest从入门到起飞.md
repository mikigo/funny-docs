
# Pytest 从入门到起飞

```shell
# ==================================
# Author : mikigo
# ==================================
```

## 一、简介

Pytest 是一个流行的基于 Python 的自动化测试框架，以其灵活性、可扩展性、易用性俘获了大批 Python 程序员的心。网上关于 pytest 的教程不少，但是都是零散的知识点，几乎没有很全面的教程，当初学习它的时候就苦于没有全面的教程而不得不去研读它的官方文档，看完一遍官方文档之后感觉还有些没弄明白，到京东上买了一本《pytest测试实战(Brian.Okken》，如获至宝，应该说是当时唯一的一个讲解 Pytest 的书籍了，看完之后我有点失望，写得也太简单了，2天就看完了，还不如看官方文档呢，就这都能出书，我都能写书了，后面又回过头来看 Pytest 官方文档。

大家知道官方文档确实是最全的，能够让你全方位的掌握，但是，就是因为太详细了，有些东西对于99.9%的使用者来说，其实没必要掌握。经过长期摸索，我将我们经常使用到的、核心的内容总结成这篇教程，希望能以一种轻松、简单、令人愉悦的方式，将这些内容讲清楚。

也希望通过讲解各个模块的知识，潜移默化的让你理解 Pytest 的 Plugin 设计哲学。

## 二、安装

<div class="termy">

```console
pip3 install pytest
---> 100%
```

</div>

只需要这样安装一下就行了，够简单易用吧。

## 三、用例编写

### 1、函数式

```python
def test_001():
    ...
    
def test_002():
    ...
```

这种是函数式的用例写法，就是直接在 py 文件里面定义函数，函数里面写测试用例。

### 2、类式

```python
class TestMikigo:

    def test_001(self):
        ...

    def test_002(self):
        ...
```

这种写法是基于类的用例写法，在函数里面写测试用例即可。

两种写法都是可以的，在执行的时候都能被 pytest 识别为用例。

从工程的角度，我更推荐使用基于类的用例写法，因为函数式的写法不能使用类级别的 fixture，因为它没有类。基于类的用例写法给我们提供了更加灵活的 fixture 的处理，让你在应对复杂测试场景的时候，游刃有余。

## 四、fixture

fixture 翻译过来是 “夹具”，简单讲就是用例执行前后要做的操作，我们称为前置（setup）和后置（teardown）操作。用例就像夹心饼干一样被夹在中间。

Pytest 灵活性很重要的一方面就是体现在它的 fixture，那是相当的灵活。不仅支持多个级别，各个级别的写法还支持多样，还可以共享、默认调用、指定调用，很多骚操作，现在不知道没关系，看完这一章应该能有所收获。

### 1、级别

总共有四个级别：函数级别（funciton）、类级别（class）、模块级别（module）、会话级别（session）

这部分只需要理解概念，不需要纠结与具体的写法。

- 函数级别（funciton）

  函数就是用例，函数级别的fixture就是在**每个**用例执行前后的操作，即： `function_setup`  `test_case`  `function_teardown` 。

- 类级别（class）

  类级别就是在**每个**用例类执行前后要执行的操作，注意，一个类只执行一次哦。

  - 如果一个类里面只有一个函数，类级别相对于函数级别，就是在函数级别前后执行，即：`class_setup`  `function_setup`  `test_case`  `function_teardown`  `class_teardown` 。

    你看其实就是在前面函数级别的基础之上外面加了一层，很好理解是吧。

  - 如果一类里面有多个函数，执行的顺序是：`class_setup`  `function_setup`  `test_case_001`  `function_teardown`    `function_setup`  `test_case_001` `function_teardown`  `class_teardown` 。

    你注意看区别，中间有多个用例函数，每个函数外都夹了一个函数级别的fixture，然后类级别fixture是放在最外层的。

- 模块级别（module）

  理解了前面类级别的fixture之后，相信你已经能推理出来了，模块其实可以理解成一个 py 文件，在一个 py 文件里面可以写多个类，每个类里面可以写多个函数。一层夹一层的。
  
- 会话级别（session）

  这个相对来讲有点抽象，其实就是你执行一次用例就是一次会话，当然一次会话里面可能只有一个用例，也可能包含多个用例模块、多个用例类、多个用例。

### 2、不同的写法

这里骚操作就比较多了，看准了哈。

#### 2.1、XUnit 的写法

熟悉 `unittest` 框架的人都知道，`unittest` 里面 `fixture` 的写法是 `setUp` 和 `tearDown`，`setUp_class` 和 `tearDown_class`，只有这一种写法，而且是固定的写法哈。

`Pytest` 是兼容 `unittest` 的，当然也支持这样写：

```python
from datetime import datetime
from time import sleep
from unittest import TestCase
class TestMikigo(TestCase):

    def setUp(self):
        print("我是前置", datetime.now())
        sleep(1)

    def test_001(self):
        print("我是用例", datetime.now())
        sleep(1)

    def tearDown(self):
        print("我是后置", datetime.now())
```

注意是继承了 `unittest.TestCase` 的，`Pytest` 可以兼容运行的，基本操作哈。

除此之外还有一些你没见过的 `Xunit` 写法：

```python
from datetime import datetime
from time import sleep
class TestMikigo:

    def setup(self):
        print("我是前置", datetime.now())
        sleep(1)

    def test_001(self):
        print("我是用例", datetime.now())
        sleep(1)

    def teardown(self):
        print("我是后置", datetime.now())
```

```console
我是前置 2022-01-24 16:17:59.267900
我是用例 2022-01-24 16:18:00.269282
我是后置 2022-01-24 16:18:01.270688
```

你看，`setup` 和 `teardown` 这种写法也是会被自动识别的。

还有这种，看准了哈：

```python
from datetime import datetime
from time import sleep
class TestMikigo:

    def setup_method(self):
        print("我是前置", datetime.now())
        sleep(1)

    def test_001(self):
        print("我是用例", datetime.now())
        sleep(1)

    def teardown_method(self):
        print("我是后置", datetime.now())
```

```console
我是前置 2022-01-24 16:24:57.456212
我是用例 2022-01-24 16:24:58.457273
我是后置 2022-01-24 16:24:59.458097
```

`setup_method` 和 `teardown_method` 也可以。

这里还要讲一下 `setup_method` 和 `setup_function` 的区别，`setup_function` 是在基于函数的用例写法时使用的，`setup_method` 是基于类的用例写法使用的，我面试别人的时候喜欢问这两个的区别，如果知道这个的，基本对本部分内容是了解的。

以上只是用例级别的，下面说下类级别的写法：

```python
from datetime import datetime
from time import sleep
class TestMikigo:

    def setup_class(self):
        print("我是类前置", datetime.now())
        sleep(1)

    def setup_method(self):
        print("我是用例前置", datetime.now())
        sleep(1)

    def test_001(self):
        print("我是用例", datetime.now())
        sleep(1)

    def teardown_method(self):
        print("我是用例后置", datetime.now())
        sleep(1)

    def teardown_class(self):
        print("我是类后置", datetime.now())
```

```console
我是类前置 2022-01-24 16:31:59.411548
我是用例前置 2022-01-24 16:32:00.411892
我是用例 2022-01-24 16:32:01.413373
我是用例后置 2022-01-24 16:32:02.414377
我是类后置 2022-01-24 16:32:03.415521
```

直接写成 `setup_class` 就可以了，在 `unitest` 里面类级别的是需要加类方法装饰器 `@classmethod` 的，`pytest` 里面可加可不加，看你喜欢。

模块级别的就用 `setup_module`，会话级别的就用 `setup_session`，这都好理解，这里就不举例了。

#### 2.2、fixture 写法

前面 `Xunit` 的写法已经很灵活了，但是 `Pytest` 真正厉害的是它自己特有的 fixture 写法。

```python
from datetime import datetime
from time import sleep
import pytest
class TestMikigo:

    @pytest.fixture(scope="function")
    def do_something_before(self):
        print("我是用例前置", datetime.now())
        sleep(1)
        yield
        print("我是用例后置", datetime.now())

    def test_001(self, do_something_before):
        print("我是用例", datetime.now())
        sleep(1)
```

这里有几点要注意：

- fixture 必须要加`@pytest.fixture()` 装饰器；

- scope 为 fixture 级别；

- fixture 的函数名 `do_something_before` 可以自定义，但是不要和 `Xunit` 的函数名一样，不然就乱掉了。

- yield 之前是前置，yield 之后是后置，这里实际上是利用了生成器的原理；

- 函数名 do_something_before 需要显式的传入用例参数：

  ```python
  def test_001(self, do_something_before):
      print("我是用例", datetime.now())
      sleep(1)
  ```
  
  或者使用 `@pytest.mark.usefixtures()` ，就像这样：
  
  ```python
  @pytest.mark.usefixtures("do_something_before")  # 也可以放到类名前面，表示对这个类里面所有的用例都生效。
  def test_001(self):
      print("我是用例", datetime.now())
      sleep(1)
  ```
  
  不过这种写法我个人不建议哈，字符串的形式属于硬编码，不好维护。

这里要好好理解一下哈，短短的几句话，其实包含了很多内容哦。这种写法没有一个严格的定式，更多是一种模式。

## 3、共享

fixture 共享是 Pytest 的一大特点，也是它灵活性的重要体现。

#### 3.1、用例之间共享

我们经常遇到多个用例需要用到同一个 fixture ：

```python
from datetime import datetime
from time import sleep
import pytest

class TestMikigo:

    @pytest.fixture(scope="function")
    def do_something_before(self):
        print("我是用例前置", datetime.now())
        sleep(1)
        yield
        print("我是用例后置", datetime.now())

    def test_001(self, do_something_before):
        print("我是用例001", datetime.now())
        sleep(1)

    def test_002(self, do_something_before):
        print("我是用例002", datetime.now())
        sleep(1)
```



```console
我是用例前置 2022-01-24 18:36:52.039974
我是用例001 2022-01-24 18:36:53.041396
我是用例后置 2022-01-24 18:36:54.042808

我是用例前置 2022-01-24 18:36:54.043354
我是用例002 2022-01-24 18:36:55.044742
我是用例后置 2022-01-24 18:36:56.046134
```

你看，我们只定义了一个 fixture，然后将它的函数名 do_something_before 分别都传给了两个用例，这样它就对两个用例都生效了。

那有同学要问了，我如果有很多的用例，每个用例都要传入参数，好麻烦嘞，有没有更妙的写法？

当然有：

```python
from datetime import datetime
from time import sleep
import pytest

class TestMikigo:

    @pytest.fixture(scope="function",autouse=True)
    def do_something_before(self):
        print("我是用例前置", datetime.now())
        sleep(1)
        yield
        print("我是用例后置", datetime.now())

    def test_001(self):
        print("我是用例001", datetime.now())
        sleep(1)

    def test_002(self):
        print("我是用例002", datetime.now())
        sleep(1)
```

`@pytest.fixture` 里面有个参数 `autouse` ，就是自动使用，默认是 `False`，我们传 `True` 就表示对当前作用域下的所有用例都生效。这个 “作用域” 要看这个 fixture 做处的位置，比如例子中，fixture 是在类里面，它就对这个类中的所有用例都生效，如果你把它放到模块里面，它对这个模块里的所有用例都生效。

`autouse` 一定要慎用，处理不好的话会引起执行逻辑的混乱，就是你会发现有些用例莫名奇妙，不知道在执行什么，可能就是有其他没注意到的 fixture 生效了。

#### 3.2、用例类之间共享

前面的例子都是将 fixture 放在类里面，这样只能对这一个类里面的用例生效，要实现用例类之间共享，就不能写在某一个类的里面了：

```python
from datetime import datetime
from time import sleep
import pytest


@pytest.fixture(scope="function", autouse=True)
def do_something_before():
    print("我是用例前置", datetime.now())
    sleep(1)
    yield
    print("我是用例后置", datetime.now())

class TestMikigo001:

    def test_TestMikigo001_001(self):
        print("我是用例TestMikigo002001", datetime.now())
        sleep(1)

class TestMikigo002:

    def test_TestMikigo001_001(self):
        print("我是TestMikigo002用例001", datetime.now())
        sleep(1)
```

我们将 fixture 写在module 里面，这样就对文件里面的所有用例都生效。

#### 3.3、超级共享

conftest.py 相当于是 Pytest 的一个本地插件库，你可以在用例的目录结构中任意位置新建一个 conftest.py 文件，然后在里面写入 fixture，这些 fixture 可以对这个 conftest.py 文件对当前目录及子目录下的所有用例生效，所以我称之为“超级共享”，而且各个目录都可以有自己的 conftest.py。

“超级共享” 不是官方术语，是我自创的哈。

咱们来新建一个 conftest.py 文件：

```console
.
├── conftest.py
└── test_case_001.py
```

在 conftest.py 文件中写一个 fixture：

```python
import pytest

@pytest.fixture(scope="function", autouse=True)
def do_something():
    print("我是用例前置", datetime.now())
    sleep(1)
    yield
    print("我是用例后置", datetime.now())
```

用例：

```python
class TestMikigo:

    def test_case_001(self):
        print("test case 001")
```

在根目录使用 `pytest -s -v` 执行一下：

```console
我是最外层用例前置 2022-02-08 16:20:39.605921
test case 001
我是最外层用例后置 2022-02-08 16:20:40.606656
```

这样当前目录下哪怕有多个用例文件，里面有成千上万条用例，执行时都会加载这条fixture，你说是不是超级共享。

### 4、顺序

前面讲“超级共享”提到，我们可以把 fixture 写在 conftest.py 文件里面，conftest.py 文件对当前目录及子目录下的所有用例生效，而各个目录都可以有自己的 conftest.py，用例文件里面还可以写 fixture，那写了这么多 fixture，它的执行顺序是怎样的，怎么去解除一些作用，这个问题非常重要，理不清楚的话，在实际项目中你会发现这条用例都在干嘛，它为什么执行这个。

跟上思路哈。

首先，从层级上来讲仍然是：会话级别（session）—> 模块级别（module）—> 类级别（class）—> 函数级别（funciton）这样的执行顺序。

然后，相同层级的情况下，要看 fixture 的位置，简单讲就是：外层 fixture 先执行。

我们以 function 级别的 fixture 举例，构造一个多层级的 fixture，建议你在本地按照下面的描述自己建一个demo，不然可能需要你有比较强的结构化思维：

```console
.
├── cases_1
│   ├── cases_1_1
│   │   ├── conftest.py   # cases_1_1 目录下 conftest
│   │   └── test_cases_1_1.py  # 用例
│   └── conftest.py  # cases_1 目录下 conftest
└── conftest.py  # 最外层 conftest

```

最外层 conftest：

```python
from datetime import datetime
from time import sleep
import pytest

@pytest.fixture(scope="function", autouse=True)
def do_something():
    print("我是最外层用例前置", datetime.now())
    sleep(1)
    yield
    print("我是最外层用例后置", datetime.now())
```

cases_1 目录下 conftest：

```python
from datetime import datetime
from time import sleep
import pytest

@pytest.fixture(scope="function", autouse=True)
def do_something_1():
    print("我是 cases_1 层用例前置", datetime.now())
    sleep(1)
    yield
    print("我是 cases_1 层用例后置", datetime.now())
```

cases_1_1 目录下 conftest：

```python
from datetime import datetime
from time import sleep
import pytest

@pytest.fixture(scope="function", autouse=True)
def do_something_1_1():
    print("我是 cases_1_1 层用例前置", datetime.now())
    sleep(1)
    yield
    print("我是 cases_1_1 层用例后置", datetime.now())
```

用例里面：

```python
from datetime import datetime
from time import sleep

import pytest


@pytest.fixture(scope="function", autouse=True)
def do_something_out():
    print("我是用例类外面前置", datetime.now())
    sleep(1)
    yield
    print("我是用例类里外面后置", datetime.now())

class TestMikigo:

    @pytest.fixture(scope="function", autouse=True)
    def do_something_in(self):
        print("我是用例类里面前置", datetime.now())
        sleep(1)
        yield
        print("我是用例类里面后置", datetime.now())

    def test_cases_1_1(self):
        print("我是测试用例 1_1")
```

这样我们就在不同层级写了一些 function 级别的 fixture，执行一下就可以清楚的看到。

```console
我是最外层用例前置 2022-02-08 15:38:52.924602
我是 cases_1 层用例前置 2022-02-08 15:38:53.925916
我是 cases_1_1 层用例前置 2022-02-08 15:38:54.927332
我是用例类外面前置 2022-02-08 15:38:55.928774
我是用例类里面前置 2022-02-08 15:38:56.930258
我是测试用例 1_1
我是用例类里面后置 2022-02-08 15:38:57.933010
我是用例类里外面后置 2022-02-08 15:38:57.933135
我是 cases_1_1 层用例后置 2022-02-08 15:38:57.933211
我是 cases_1 层用例后置 2022-02-08 15:38:57.933277
我是最外层用例后置 2022-02-08 15:38:57.933338
```

从上到下，你仔细看之后，结论呼之欲出：**外层先执行**。

外层 conftest 先于内层 conftest，内层 conftest 先于类外面的，类外面的先于类里面的。

所以我们在写fixture的时候一定要特别注意，Pytest 给我们提供的很灵活很方便的fixture的各种写法，特别是加了 `autouse=True` 之后，如果你搞不清楚fixture哪个先执行哪个后执行，那你最好就别用这些写法，老老实实用 Xunit 的写法，已经能满足多大部分项目需求了。

注意，以上我们写的这些fixture的函数名都是不同的，如果是相同的函数名会出现什么情况呢？

咱们把 `do_something_out` 改成 `do_something_in` ，两个 fixture 函数名都是 `do_something_in`，我们看看会发生什么。

```console
我是最外层用例前置 2022-02-08 15:56:03.138015
我是 cases_1 层用例前置 2022-02-08 15:56:04.138356
我是 cases_1_1 层用例前置 2022-02-08 15:56:05.139590
我是用例类里面前置 2022-02-08 15:56:06.140796
我是测试用例 1_1
我是用例类里面后置 2022-02-08 15:56:07.142623
我是 cases_1_1 层用例后置 2022-02-08 15:56:07.142667
我是 cases_1 层用例后置 2022-02-08 15:56:07.142694
我是最外层用例后置 2022-02-08 15:56:07.142715
```

你看，类外面的 `do_something_in` 没有执行，说明相同函数名的 fixture，只会执行内层的。

这点知识也非常重要哈，因为在实际项目中，我们经常会遇到有些用例我不想用某些外层的 fixture，于是我们可以在内层定义一个同名的 fixture，里面写pass，相当于抵消掉了外层 fixture 的作用。

## 五、断言

### 1、常规断言

Pytest 本身并没有提供断言的方法，而是直接使用Python自带的 assert 语句进行断言。

```python
def test_case_001():
    assert 1 == 1
```

assert 后面直接写表达式就好了，so easy!

### 2、自定义断言

使用 assert 断言很简单，但是抛的异常日志基本没什么参考意义，因为在断言失败的时候，只会提示你 assert 后面的表达式不成立，这不是废话吗，肯定不成立才断言失败噻，问题是我的表达式可能是一些比较复杂的封装，这里面具体什么问题就不知道了。因此，使用自定义断言会比较好。

从本质上讲，断言失败实际上都是捕获的 `AssertionError（断言异常）`，所以我们只需要定义一个自定义异常类，然后抛一个 `AssertionError` 就可以了。

```python
class AssertCommon:
    
    @staticmethod
    def assert_true(expect):
        """断言为真"""
        if not expect:
            raise AssertionError(f"<{expect}>不为真")
```

通过给 AssertionError 传入自定义的字符串，用例失败时，我们就可以看到明确的失败信息。

## 六、命令行参数

使用 Pytest 执行用例时，我们经常都是通过命令行来执行的，有同学要说了，我一般是通过编辑器里面直接就执行了；在实际项目中编写用例调试用例，使用编辑器执行用例没问题，但在 CI 集成环境下，一般是需要用命令行的。

Pytest 要想玩得溜，命令行参数必须要熟悉，Pytest 支持的参数很多，有自带的参数，插件提供的参数，还有我们自己定义的一些参数，下面就介绍在项目中常用的参数：

### 1、-s

有时候你发现在用例里面使用 print 语句，但是执行的时候却没有打印，那多半是因为你没有加这个参数。等价于 `--capture=no`，用途就是捕获 print 输出。如果你不知道 `capture` 参数也没关系，不重要。

### 2、-v

详细展示终端输出。比详细更详细使用 `-vv` ，我们当然是希望输出信息越详细越好。

### 3、-k

执行用例的时候非常有用，通过关键词来匹配用例，用例的关键词有很多，模块名、文件名、类名、函数名都是关键词，比如：

```console
pytest -k "test_music"
```

表示执行所有包含 `test_music` 关键词的用例。

-k 还有一点可能好多同学都不知道，它还支持逻辑表达式，比如：

```console
pytest -k "test_music or test_movie"
```

```console
pytest -k "not test_music and not test_movie""
```

逻辑表达是支持 `and/or/not` 的逻辑组合。

在批量支持用例时，我们通常是不需要执行全量用例的，学会精准的组装用例集对于自动化测试非常重要。

### 4、-m

我们可以给用例打上标签（mark）：

```python
import pytest

class TestMikigo:
    
    @pytest.mark.smoke
    def test_case_001(self):
        ...
```

使用装饰器 `@pytest.mark` 点后面加标签名，就可以给用例打标签，标签名随意指定，甚至可以用中文。

打完标签之后，批量执行用例时就可以通过标签来加载用例，用法和 -k 是一样的。

```console
pytest -m "smoke or core"
```

### 5、--co

这个参数全称是 `--collect-only`，表示只收集用例，不执行。

每周我需要给老板汇报目前所有用例多少条，咱总不可能在代码里面一条条去数吧，我通常会使用：

```console
pytest --co
```

直接就可以看到加载了多少条用例。

另外，有时候批量修改了一些代码，可能引起一些错误，我们可以通过执行 `pytest --co`  来快速检测一下是否存在错误，因为 Pytest 在加载用例的时候同时也会检测代码中存在的一些问题。这个也非常好用。

### 6、maxfail

配置最大失败次数，如果一次执行出现了大量的失败，多半这次测试是无效的，通过配置这个参数，我们不用等到所有用例执行完才结束，尽早结束节约时间。

```console
pytest --maxfail=int_number
```

这里的 int_number 就是最大的失败次数，你可以根据你的经验来指定一个数字。

我的方案是先获取到本次要执行的总用例数 `collected_cases_num`，然后配置一个总数的比例，如 0.5，表示只要失败次数达到了总数的一半，就可以直接结束测试。

```console
pytest --maxfail=int(collected_cases_num * 0.5)
```

这样做的好处是，随着项目中用例数量的增加，我不需要去修改这个最大失败的数据，而是通过配置整体的失败比例，这样做更加合理，也更易于维护。

### 7、reruns

失败重跑次数，在自动化测试过程中经常会有一些不确定性，网络问题、环境问题、量子力学、地球引力等等都有可能造成用例失败，特别是 UI 自动化测试，这些情况经常发生，为了尽量排除环境问题造成的用例失败，采用失败后自动重跑是一个比较好的方案。

```console
pytest --reruns=2
```

表示失败后重跑2次，如果后面重跑用例成功了，最终的用例状态为 PASSED。

这个参数需要安装三方插件：

```console
sudo pip3 install pytest-rerunfailures
```

### 8、timeout

用例超时在 CI 流程中非常重要，因为所有的每日构建都应该是有时长限制的，一跑就是两三天不停就不叫每日构建了，用例执行过程中可能存在一些异常情况，导致用例卡住不动，或者执行速度变慢，我们使用 `--timeout` 可以给每条用例设置一个最大的时长，如果超时没有执行完，就是强制停止用例。

```console
pytest --timeout=200
```

表示每条用例的超时时间为 200 秒，注意单位是秒哦。

这个参数需要安装三方插件：

```console
sudo pip3 install pytest-timeout
```

### 9、自定义命令行参数

以上参数都是 Pytest 自带的或者三方插件给我们提供的参数，当这些参数不能满足我们的需求的时候我们就需要自定义一些命令行参数。

首先，我们需要注册命令行参数，前面讲超级共享的时候讲了 conftest.py，但是 conftest.py 能做的事情可不仅仅是写点 fixture，它可是 Pytest 的本地插件，在里面我们可以写 hook（钩子）函数，这里我们介绍其中一个 hook 函数，即实现自定义命令行参数的 hook 函数，其他的 hook 函数我们后面会介绍到。

官方说法是：注册命令行选项。实际就是自定义命令行参数。

举例：

```python
def pytest_addoption(parser):
    parser.addoption()
```

`parser.addoption()` 里面可以传入挺多参数的，但是不是所有的都需要：

```console
1、name：自定义命令行参数的名字，可以是："foo"， "-foo" 或 "--foo"；
2、action：在命令行中遇到此参数时要采取的基本操作类型；
3、nargs：应该使用的命令行参数的数量；
4、const：某些操作和nargs选择所需的常量值；
5、default：如果参数不在命令行中，则生成的默认值。
6、type：命令行参数应该转换为的类型；
7、choices：参数允许值的容器；
8、required：命令行选项是否可以省略（仅可选）；
9、help：对参数作用的简要说明；
10、metavar：用法消息中参数的名称；
11、dest：要添加到 parse_args() 返回的对象中的属性的名称；
```

常用的几个参数就这几个，以下是项目实例：

```python
def pytest_addoption(parser):
    parser.addoption(
        "--logLevel",
        action="store",
        default="DEBUG",
        help="DEBUG, INFO，WARNING，ERROR, CRITICAL, 终端日志输出级别",
    )
```

用于控制日志输出的级别，CI 集成环境下我们不需要输出 DEBUG 级别的日志，我们可以这样用：

```console
pytest --logLevel=INFO
```

这样在执行用例的时候，参数就可以传递进来，那么传递进来之后，我们在哪里用？

同样是在 conftest.py 里面：

（1）通过 fixture 里面的 request 对象：

```python
@pytest.fixture(scope="session")
def do_something(request):
    logLevel = request.config.getoption("--logLevel")
```

这样可以获取到，`request.config.getoption` 是固定写法，经常有同学问你咋知道可以这么用呢，在哪里可以看到，实际上可以通过给 `request` 打断点，你会看到这个对象内有哪些方法。

（2）通过 hook 函数里面的 seesion 对象：

```python
def pytest_sessionstart(session):
    logLevel = session.config.option.logLevel
```

这里的 hook 函数不一定是 `pytest_sessionstart`，好多 hook 函数都可以。

（3）通过 hook 函数里面的 item 对象：

```python
def pytest_runtest_teardown(item):
    logLevel = item.session.config.option.logLevel
```

（4）在用例中使用：

```python
def test_xxx(pytestconfig):
    log_level = pytestconfig.option.logLevel
```

`pytestconfig` 是 `pytest` 提供的一个内容 `fixture` ，可以获取到所有的参数；获取参数值的方法除了 `pytestconfig.option.logLevel` 这种写法，`pytestconfig.getoption("logLevel")` 这种写法也是 ok 的。

仔细观察，获取命令行参数都在 config 这个对象里面，以上举例的不同的 hook 函数默认的参数是不同的。

## 七、参数化

参数化是自动化测试里面非常重要的一个特性，特别是对于接口自动化测试，那是肯定要用到的。我看到很多网上的教程将参数化称为高级技能，通过这点能看出来，高级也不咋的哈。

Pytest 的参数化使用方法也很简单，使用装饰器：

```python
@pytest.mark.parametrize("par_1", [1, 2])
def test_case_001(par_1):
    ...
```

- 装饰器是固定用法 `@pytest.mark.parametrize`，记住就行了，记不住就记住两个东西，首先是在 mark 里面，然后 p 开头，最后用编辑器补全就好了。

- 参数有 3 个：

  - 第 1 个参数是字符串类型，里面是参数的变量名称，多个变量需要用逗号分隔；

    这也是最常见的用法，网上教程基本都是这样讲的，但如果你看过 Pytest 源代码这个参数类型是这样定义的： `argnames: Union[str, List[str], Tuple[str, ...]]` 说明列表和元组也可以，只要里面是字符串就行。

  - 第 2 个参数是一个列表，准确的讲是一个可迭代对象，一般咱们就用列表好了，如果是多个参数就是 2 维列表，列表中每个元素的个数对应变量的个数。
  
    ```python
    @pytest.mark.parametrize("par_1, par_2", [[1, 2], [3, 4]])
    def test_case_001(par_1， par_2):
        ...
    ```
  
    这个参数虽然是可迭代对象，但你最好别使用随机工具生成（每次都是随机数），这可能影响重跑失败用例等一些功能，也最好别使用生成器放里面。
  
  - 第 3 个参数是 ids，这个参数是标记 ID 的，不传也可以，区别就是不传的话终端输出的用例标题会自动加上参数，可能好多同学没用过，不理解也没关系哈，本身用的不多。

用例的参数化用法就是这么简单。

Pytest 其实还支持 fixture 的参数化，这也是 fixture 相对于 Xunit 写法的其中一点优势，但在实际项目中很少用，没有太多这样的需求，这里就不讲了。

## 八、Hook（钩子）函数

hook 函数相当于是 Pytest 的一些本地插件，Pytest 给我们提供了许多的 hook 函数，用于处理不同阶段的自定义行为。

有几个注意点：

- hook 函数一般不建议写在非根目录下的 conftest 插件文件里面，我们一般是写在最外层的那个 conftest 里面。
- hook 函数都是以 ` pytest_` 开头的函数。
- 不同的 hook 函数有它自己的功能和所属的阶段。

### 1、hook 函数略览

Pytest 内置了许多的 hook 函数供我们使用，下面我们就按照阶段划分，罗列一下有哪些 hook 函数，可以大致感受一下：

引导钩子：

```python
pytest_load_initial_conftests
pytest_cmdline_preparse
pytest_cmdline_parse
pytest_cmdline_main
```

初始化钩子：

```python
pytest_addoption
pytest_addhooks
pytest_configure
pytest_unconfigure
pytest_sessionstart
pytest_sessionfinish
pytest_plugin_registered
```

收集钩子：

```python
pytest_collection
pytest_collect_directory
pytest_collect_file
pytest_pycollect_makemodule
pytest_pycollect_makeitem
pytest_generate_tests
pytest_make_parametrize_id
pytest_collection_modifyitems
pytest_collection_finish
```

测试运行（runtest）钩子：

```python
pytest_runtestloop
pytest_runtest_protocol
pytest_runtest_logstart
pytest_runtest_logfinish
pytest_runtest_setup
pytest_runtest_call
pytest_runtest_teardown
pytest_runtest_makereport
pytest_pyfunc_call
```

报告钩子：

```python
pytest_collectstart
pytest_make_collect_report
pytest_itemcollected
pytest_collectreport
pytest_deselected
pytest_report_header
pytest_report_collectionfinish
pytest_report_teststatus 
pytest_terminal_summary
pytest_fixture_setup
pytest_fixture_post_finalizer
pytest_warning_recordedLiteral 
pytest_runtest_logreport
pytest_assertrepr_compare
pytest_assertion_pass
```

调试钩子：

```python
pytest_internalerror
pytest_keyboard_interrupt
pytest_exception_interact
pytest_enter_pdb
```

这些钩子函数都是 Pytest 给我们提供的，你可以在 conftest 插件文件里面去重写函数来实现你的自定义功能。

看到这么多函数先别慌，咱不需要掌握所有的，因为很多是不常用的，也就是我开篇提到的 99% 的人都用不到的，其中经常使用到的一些比较常用的 hook 函数，将会在后续内容介绍到。

### 2、常用的 hook 函数

#### 2.1、pytest_addoption

这个 hook 函数在前面将自定义命令行参数的时候已经用过了，它的用途就是注册命令行参数，这些值在测试运行开始时会被调用一次。

```python
# conftest.py

def pytest_addoption(parser):
    parser.addoption()
```

前面有例子，这里就不多讲了，用法很简单。

它都是通过 `parser.addoption` 在定义命令行参数的。

#### 2.2、pytest_configure

这个函数主要是用来获取命令行参数的：

```python
# conftest.py

def pytest_configure(config):
    my_option = config.getoption("--opt")
```

是在执行测试执行运行，简单哈。

`pytest_unconfigure` 则是在执行测试退出之前运行。

#### 2.3、pytest_sessionstart

这个函数在 session 对象创建之后，执行收集之前调用：

```python
def pytest_sessionstart(session):
    """
    :param pytest.Session session: The pytest session object.
    """
```

session 对象里面有很多属性，常用的：

- startdir：用例根目录的绝对路径。
- items：用例对象的列表。
- config：config对象。

你也可以往里面动态添加一些属性。

和它对应的 `pytest_sessionfinish` 是在所有测试结束，退出之前执行。

#### 2.4、pytest_collection_modifyitems

这个函数主要用来调整用例：

```python
# conftest.py

def pytest_collection_modifyitems(session, config, items):
    """
    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
```

- session 为 Pytest 的 session 对象。

- config 为 Pytest 的 config 对象。

- items 是一个列表，其他每个元素就是一个用例对象。

  item 里面有很多属性，常用的：

  ```console
  name：用例的名称
  nodeid：从用例根目录开始到用例文件的路径
  own_markers：用例的mark标签
  ```

`pytest_collection_finish` 则是在收集完并且修改完之后运行，它是在 `pytest_collection_modifyitems` 之后的。

#### 2.5、pytest_runtest_setup

这个函数是在调用 setup 的时候运行：

```python
def pytest_runtest_setup(item):
    ...
```

注意是 item，不是 items，item 是用例对象。

比如，你可以在每次用例执行之前输出用例的标题：

```python
def pytest_runtest_setup(item):
    logger.info(item.function.__name__)
```

`pytest_runtest_call` 和 `pytest_runtest_teardown` 分别是在用例执行过程中和用例 teardown 阶段运行，用法是一样的。

#### 2.6、pytest_runtest_makereport

这个函数是用于创建测试报告的，每个测试用例的测试报告都分为 setup、call 和 teardown 三个测试阶段。如果你熟悉 allure 报告的话，应该能轻易 get 到我说的。

```python
def pytest_runtest_makereport(item):
    out = yield
    report = out.get_result()
```



## 九、测试报告

### 1、allure

Pytest 最常用的测试报告是 allure，它是一个三方插件，安装它：

```console
sudo pip3 install allure-pytest
```

使用也很简单，只需要执行时加参数 `--alluredir=xxx` 即可：

```console
pytest --alluredir=report
```

这样就能在 report 目录下生成报告，打开它你会发现 report 目录下是一堆文本文件，这咋看呢？

还没完~

你还需要安装 allure 的查看工具，你可以直接从 github上去下载最新的版本，然后安装它即可，比如我现在下来安装是这样的：

```console
sudo dpkg -i allure_2.19.0-1_all.deb
```

查看报告：

- 在线查看：

```console
allure serve report
```

- 生成本地 html

```console
allure generate report -o allure-report
```

这样在 `allure-report` 目录下会一堆文件，其中有一个 `index.html` 是报告的主文件。

使用浏览器直接打开它，你会发现没有数据！

还没完~~

使用命令打开：

```console
allure open allure-report
```

不出意外浏览器会自动打开报告。

需要说明的是，allure 可不是专门为 Pytest 开发的，经过很长时间的发展，它已经进化为一个报告框架了，能支持非常多的语言及工具生成测试报告，总之这玩意儿老狠了。想深入研究的同学看这里 [allure](https://qameta.io/allure-report/) 。

### 2、pytest-html

上古时期 Pytest 的“糟糠之妻”，尽管该项目是由 Pytest 官方在维护，但是社区热度不行了，主要是因为颜值不行，很少有人用，也不想过多的介绍它，走个过场吧。

安装：

```console
sudo pip3 install pytest-html
```

使用：

```python
pytest --html=report.html
```

### 3、xml

这是个 Pytest 自带的报告，不需要安装插件：

```console
pytest --junit-xml=report.xml
```

我个人还是非常喜欢这种报告形式的，因为它不需要安装其他插件，而且处理报告中的数据也非常简单。

## 十、Pytest 框架核心

我们通常基于 Pytest 来编写搭建我们自己的测试框架，Pytest 自然就成了我们自己测试框架的核心，那么同学们有没有想过，Pytest 的核心是什么？

相信 90% 的同学没去考虑过或者没了解过~

Pluggy 就是 Pytest 的核心框架，几乎 Pytest 所有的功能都是基于 Pluggy 实现的，这是一个被极少人知道且严重低估的框架，它到底是什么玩意儿，咱们这里简单聊一聊。

Pluggy 是从 Pytest 框架中被开发者抽取出来的，因为开发者发现他们设计的这种插件化方案，完全可用在其他的项目中，因此他们总结提炼出了 Pluggy 项目；

令人直呼“厚礼谢”的是整个 Pluggy 项目加起来也就 1100 来行代码（包含注释 ），这就是 Pytest 的核心基石，就像是 Linux 系统中的 Linux 内核的作用。理解它你才能真正理解 Pytest 插件化设计哲学。

为什么说它被低估了，github 上才不到 900 的 star，真的是深藏功与名！

咱们先随便写个函数：

```python
class Mikigo:

    def miki(self, arg1, arg2):
        """这是一个可以定制的钩子"""
```

通常，类里面的函数咱们想要重写，只需要继承这个类，然后重写覆盖函数就好了，这就是类的多态，不多讲了；

那咱们使用 Pluggy 怎么去覆盖类里面的函数呢？

```python
import pluggy

# hook 规范，用于生成一个修饰器去标记函数作为钩子函数
hookspec = pluggy.HookspecMarker("mikigo") 
# hook 实现，用于生成一个修饰器去标记函数作为钩子函数的具体实现
hookimpl = pluggy.HookimplMarker("mikigo")

class Mikigo:

    @hookspec
    def miki(self, arg1, arg2):
       """这是一个可以定制的钩子"""

class Plugin_1:

    @hookimpl
    def miki(self, arg1, arg2):
        print("我是 Plugin_1.miki()")
        return arg1 + arg2
    
# 实例化一个插件管理器对象    
pm = pluggy.PluginManager("mikigo")
# 将 Mikigo 类添加进去
pm.add_hookspecs(Mikigo)
# 注册插件类
pm.register(Plugin_1())
# 通过 hook 属性访问函数
results = pm.hook.miki(arg1=1, arg2=2)
print(results)
```

```console
我是 Plugin_1.miki()
[3]
```

你看，原来的 `Mikigo` 类里面的函数是没有执行的，而是执行了 `Plugin_1` 类里面的函数，并且获取到了返回值。

- `PluginManager` 是整个插件系统的管理器，传递一个工程名称即可进行实例化；

- `add_hookspecs` 添加一个钩子到管理器中，参数是 module 或 class 对象，底层实际是通过 `dir()` 自省函数进行遍历添加到一个 names 的容器中。
- `register`  注册插件

如果咱们还想增加一个插件呢?

```python
import pluggy

# hook 规范，用于生成一个装饰器去标记函数作为钩子函数
hookspec = pluggy.HookspecMarker("mikigo") 
# hook 实现，用于生成一个装饰器去标记函数作为钩子函数的具体实现
hookimpl = pluggy.HookimplMarker("mikigo")

class Mikigo:

    @hookspec
    def miki(self, arg1, arg2):
       "这是一个可以定制的钩子"

class Plugin_1:

    @hookimpl
    def miki(self, arg1, arg2):
        print("我是 Plugin_1.miki()")
        return arg1 + arg2
    
class Plugin_2:

    @hookimpl
    def miki(self, arg1, arg2):
        print("我是 Plugin_2.miki()")
        return arg1 - arg2
    
# 实例化一个插件管理器对象    
pm = pluggy.PluginManager("mikigo")
# 将 Mikigo 类添加进去
pm.add_hookspecs(Mikigo)
# 注册插件类
pm.register(Plugin_1())
pm.register(Plugin_2())
# 通过 hook 属性访问函数
results = pm.hook.miki(arg1=1, arg2=2)
print(results)
```

```console
我是 Plugin_2.miki()
我是 Plugin_1.miki()
[-1, 3]
```

`Plugin_2` 先执行，然后 `Plugin_1` 也执行了，两个插件的返回值也都放到一个列表里面了，是不是很神奇。

那如果想 `Plugin_1` 先执行，`Plugin_2` 后执行呢？

```python
import pluggy

# hook 规范，用于生成一个修饰器去标记函数作为钩子函数
hookspec = pluggy.HookspecMarker("mikigo")
# hook 实现，用于生成一个修饰器去标记函数作为钩子函数的具体实现
hookimpl = pluggy.HookimplMarker("mikigo")

class Mikigo:

    @hookspec
    def miki(self, arg1, arg2):
        "这是一个可以定制的钩子"

class Plugin_1:

    @hookimpl(tryfirst=True)
    def miki(self, arg1, arg2):
        print("我是 Plugin_1.miki()")
        return arg1 + arg2

class Plugin_2:

    @hookimpl(trylast=True)
    def miki(self, arg1, arg2):
        print("我是 Plugin_2.miki()")
        return arg1 - arg2

# 实例化一个插件管理器对象
pm = pluggy.PluginManager("mikigo")
# 将 Mikigo 类添加进去
pm.add_hookspecs(Mikigo)
# 注册插件类
pm.register(Plugin_1())
pm.register(Plugin_2())
# 通过 hook 属性访问函数
results = pm.hook.miki(arg1=1, arg2=2)
print(results)
```

```console
我是 Plugin_1.miki()
我是 Plugin_2.miki()
[3, -1]
```

可以通过 `tryfirst` 和 `trylast` 来控制，有同学应该有印象， Pytest hook 里面也是用 `tryfirst` 和 `trylast` 控制其 hook 函数执行的先后顺序的，其底层实现是从这里来的。

正是因为可以随意添加插件以及修改插件的执行顺序，才使得在 Pytest 中我们能灵活的定义一些 hook 函数来实现我们想要的功能，Pytest 以及其三方插件，都是基于此基本逻辑构建起来的。

这里就简单介绍一下基本原理，想要深入了解的同学点这里 [Pluggy](https://github.com/pytest-dev/pluggy)。