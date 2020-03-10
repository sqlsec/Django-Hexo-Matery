# Django-Hexo-Matery
尝试用Django3重写的我的Hexo博客，使用的前端主题是 Matery。

# 开发环境

**操作系统**：macOS Cataline 10.15.3

**Python**：[pyenv](https://www.sqlsec.com/2019/12/pyenv.html) 安装的 [pypy3.6-7.3.0](https://www.pypy.org/) (PyPy解释器平均比我们平时使用的CPython快4.4倍)

**Django**：Django 3.0.3

**前端**：https://github.com/blinkfox/hexo-theme-matery

**后台**：https://simpleui.88cto.com/simpleui/

# 前言

项目是初学Django写的，代码也没有重构，实际上个人感觉还是比较烂的，先挂Github吧，等以后Djano更熟悉了之后 会慢慢完善这个项目的。

# 相关依赖

## MySQL

macOS下Django3在连接MySQL会出一些问题，解决如下：

```bash
# 确保 pip 是最新版本
$ pip install --upgrade pip

# 临时在当前的shell环境中配置一个 openssl 变量
export LDFLAGS="-L/usr/local/opt/openssl/lib $LDFLAGS"
export CPPFLAGS="-I/usr/local/opt/openssl/include $CPPFLAGS"

$ pip install mysqlclient
```

## pillow

在`models.py`中含有`ImageField`图片类型的时候，如果`pillow`没有安装好的话 会报错：

```python
image = models.ImageField(upload_to='avatar/%Y/%m', verbose_name='头像', max_length=100)
```

解决方法是macOS下安装配置好`zlib`即可：

```bash
# 安装 zlib
$ brew install zlib

# 链接 zlib 会提示
$ brew link zlib --force

Warning: Refusing to link macOS-provided software: zlib
For compilers to find zlib you may need to set:
  export LDFLAGS="-L/usr/local/opt/zlib/lib"
  export CPPFLAGS="-I/usr/local/opt/zlib/include"
```

根据上述提示，进行如下操作：

```bash
# 临时在当前的shell环境中配置一个 zlib 变量
export LDFLAGS="-L/usr/local/opt/zlib/lib"
export CPPFLAGS="-I/usr/local/opt/zlib/include"

$ pip install pillow
```

## 分页插件

**项目地址**：https://github.com/jamespacileo/django-pure-pagination

```bash
$ pip install django-pure-pagination
```

## 导入导出

**项目地址**：https://github.com/django-import-export/django-import-export

```bash
$ pip install django-import-export
```

## markdown编辑器

**项目地址**：https://github.com/pylixm/django-mdeditor

```bash
$ pip install django-mdeditor
```

## markdowb前台解析

**项目地址**：https://github.com/lepture/mistune

```bash
$ pip install mistune
```

##  simpleui

**项目地址**：https://github.com/sea-team/simpleui

```bash
$ pip install django-simpleui
```

# 前台展示

## 首页

首页的红蓝背景 感觉还是比较简约高大上的：

![image-20200310165514043](imgs/image-20200310165514043.png)  

推荐文章栏目：

![image-20200310170504219](imgs/image-20200310170504219.png)  

首页正文：

![image-20200310170603835](imgs/image-20200310170603835.png)  

 ## 文章归档

文章日历是动态的，模仿Github的提交记录：

![image-20200310170640147](imgs/image-20200310170640147.png)  

## 文章标签

标签的背景颜色随机的，看上去不那么单一，并附带 对应的文章数目：

![image-20200310170804303](imgs/image-20200310170804303.png)    

## 文章分类

和标签基本上是一个模板做出来的，只是传入的数据不一样：

![image-20200310170907115](imgs/image-20200310170907115.png)  

## 标签数据可视化

根据文章的标签的动态数据：

![image-20200310171204282](imgs/image-20200310171204282.png)   

## 分类数据可视化

雷达图是动态展示出来的：

![image-20200310171142767](imgs/image-20200310171142767.png)  

## 关于页面

这个页面同事展示了文章分类、标签和发布时间的数据情况：

![image-20200310171246578](imgs/image-20200310171246578.png)  

## 友情链接

卡片的背景颜色和之前的标签和分类一样随机的：

![image-20200310171518141](imgs/image-20200310171518141.png)  

# 后台展示

## 后台登录界面

![image-20200310171607385](imgs/image-20200310171607385.png)

## 后台首页

![image-20200310171821937](imgs/image-20200310171821937.png)

## 文章

支持导入和导出，缩略图预览等：

![image-20200310171857493](imgs/image-20200310171857493.png)  

## 分类

分类 引入了https://fontawesome.com/icons 图片库，支持自定义图标 并进行图标预览，支持是否添加到菜单和分类菜单的排序：

![image-20200310171922853](imgs/image-20200310171922853.png)  

## 友链

友链支持列表页直接编辑，并且支持头像预览，以及支持导入和导出

![image-20200310171946090](imgs/image-20200310171946090.png)  

## 文章编辑

后台引入了Markdown编辑器，写作起来更高效：

![image-20200310172058764](imgs/image-20200310172058764.png)  

 文章的缩略图预览也添加到编辑文章的下方了：

![image-20200310172220223](imgs/image-20200310172220223.png)  

# TO DO

- [ ] 整站访客数量统计
- [ ] 文章评论功能
- [ ] 网站搜索功能
- [ ] RSS订阅生成
- [ ] sitemap生成
- [ ] 不同页面的SEO优化
- [ ] 后台里面可以设置网站邮箱之类的变量值
- [ ] 文章按照月份归档功能
- [ ] 缓存加速
- [ ] 网站部署文档