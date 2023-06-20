# Linux 上如何选择用 pip3 还是 sudo pip3

## （1）sudo pip3

如果这个包是带有**命令行工具**的，推荐使用`sudo pip3 install xxx` 进行安装;

这样命令行工具才能写入到系统目录下，一般是在 `/usr/local/bin/` 下面；

> 如果你没有加 `sudo` 安装，命令行工具无法写入到系统目录下，而是写入到 `$HOME/.local/bin`，这个路径很明显不是系统的环境变量，因此无法**直接**使用此命令，要想使用它你有**两种**方法：
>
> 第一种：
>
> ```shell
> # 进入到命令目录 
> cd $HOME/.local/bin/
> # 给命令执行赋权限
> sudo chmod +x mycmd
> # 执行它
> ./mycmd
> ```
>
> 第二种：
>
> 将 `$HOME/.local/bin` 添加到 `PATH` 里面:
>
> 临时修改：
>
> ```shell
> export PATH=/home/uos/.local/bin:$PATH
> #或者把PATH放在前面
> export PATH=$PATH:/home/uos/.local/bin
> ```
>
> 用户级别永久修改：
>
> ```shell
> vim ~/.bashrc
> # 在最后一行加上
> export PATH=$PATH:/home/uos/.local/bin
> ```
>
> 系统级别永久修改：
>
> ```shell
> vim ~/.bash_profile
> # 在最后一行加上
> export PATH=$PATH:/home/uusama/mysql/bin
> ```

你看如果带命令行工具的库，安装的时候没有加 `sudo` 你要多做多少事情；

所以请记住，带有**命令行工具**的三方库，安装的时候使用 `sudo pip3 install`。

## （2）pip3

如果这个库没有命令行工具，或者说它安装过程中不需要写入系统目录，你使用 pip3 或 sudo pip3 安装都可以；

但是，我个人推荐**不要加 `sudo`**；

原因就需要介绍一点点**背景知识**：

>在 Linux 上，Python 三方包通常被安装在以下三个路径中：
>
>1. `/usr/lib/pythonX.X/site-packages`
>
>   这个路径中安装的是系统默认的 Python 解释器的三方包，X.X 代表 Python 版本号，如 2.7、3.6;
>
>2. `/usr/local/lib/pythonX.X/site-packages`
>
>   这个路径中安装的是用户自己安装的 Python 解释器的三方包，X.X 代表 Python 版本号，如 2.7、3.6;
>
>3. `$HOME/.local/lib/pythonX.X/site-packages`
>
>   这个路径中安装的是当前用户的 Python 解释器的三方包，X.X代表 Python 版本号，如 2.7、3.6;
>
>在加载Python三方包时，系统会**按照以下顺序查找三方包的路径**：
>
>1. 先查找当前工作目录是否有需要的包;想
>2. 查找 `$HOME/.local/lib/pythonX.X/site-packages`;
>3. 查找 `/usr/local/lib/pythonX.X/site-packages`
>4. 查找 `/usr/lib/pythonX.X/site-packages`
>
>如果在以上路径中找到了需要的包，就会加载它们；
>
>如果没有找到，则会抛出ImportError异常；
>
>需要注意的是，如果相同的包存在于多个路径中，系统会加载最先找到的那个包，而不是后面找到的那个包；
>
>因此，如果有多个Python解释器或版本，并且使用了不同的路径安装三方包，就需要确认加载的包是否正确。

使用 `pip3` 安装的时候是安装到 `$HOME/.local/lib/pythonX.X/site-packages` 路径下；

而使用 `sudo pip3` 安装的时候是安装到 `/usr/local/lib/pythonX.X/site-packages` 路径下

基于前面的背景知识，这个路径是排在前面的，是会被**优先加载到**；

因此，**结论：我始终推荐优先考虑使用 `pip3` 安装（不加`sudo` ）；**

有同学要问了，凭啥优先加载到，我就要用它呢？你的领导做啥都先想到你，你觉得是不是好事，你细品～～

---------------



