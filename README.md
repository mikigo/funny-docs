# funny-docs

使用mkdocs构建文档系统，记录一些有趣的知识；

不积跬步无以至千里，不积小流无以成江海。

## 安装
```shell
pipenv install
```

安装完成之后：

pipenv shell

进入虚拟环境；

## 在线开发预览
mkdocs serve

编辑markdown文件就可以及时查看网站显示效果；

## 编译打包
mkdocs build

编译完成之后会在根目录下生成一个site目录，里面报告编译后的文件；

可以将编译打包之后的文件(site目录)部署到任意HTTP服务，即可，通过浏览器访问；

## markdown文档编写规范
1.md文档按照现有目录结构存放；

2.新增文档注意在yml文件里面添加配置；

3.图片资源存放在img目录下，可参考现有目录划分结构；