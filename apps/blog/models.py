from datetime import datetime
from django.db import models
from django.utils.html import format_html
from mdeditor.fields import MDTextField


class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(max_length=30, verbose_name='标签名称')

    # 统计文章数 并放入后台
    def get_items(self):
        return len(self.article_set.all())

    get_items.short_description = '文章数'

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=99, verbose_name='分类排序')
    active = models.BooleanField(default=True, verbose_name='是否添加到菜单')
    icon = models.CharField(max_length=30, default='fa-home',verbose_name='菜单图标')

    # 统计文章数 并放入后台
    def get_items(self):
        return len(self.article_set.all())

    def icon_data(self):
        return format_html(
            '<i class="{}"></i>',
            self.icon,
        )

    get_items.short_description = '文章数'
    icon_data.short_description = '图标预览'

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.TextField(max_length=100, verbose_name='文章描述')
    cover = models.CharField(max_length=200, default='https://image.3001.net/images/20200304/15832956271308.jpg', verbose_name='文章封面')
    content = MDTextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='文章分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')

    def cover_data(self):
        return format_html(
            '<img src="{}" width="156px" height="98px"/>',
            self.cover,
        )

    def cover_admin(self):
        return format_html(
            '<img src="{}" width="440px" height="275px"/>',
            self.cover,
        )

    def viewed(self):
        """
        增加阅读数
        """
        self.click_count += 1
        self.save(update_fields=['click_count'])

    cover_data.short_description = '文章封面'
    cover_admin.short_description = '文章封面'

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    文章评论
    """
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章', on_delete=models.CASCADE)
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:20]


class Links(models.Model):
    """
    友情链接
    """
    title = models.CharField(max_length=50, verbose_name='标题')
    url = models.URLField(verbose_name='地址')
    desc = models.TextField(verbose_name='描述', max_length=250)
    image = models.URLField(default='https://image.3001.net/images/20190330/1553875722169.jpg', verbose_name='头像')

    def avatar_data(self):
        return format_html(
            '<img src="{}" width="50px" height="50px" style="border-radius: 50%;" />',
            self.image,
        )

    def avatar_admin(self):
        return format_html(
            '<img src="{}" width="250px" height="250px"/>',
            self.image,
        )

    avatar_data.short_description = '头像'
    avatar_admin.short_description = '头像预览'

    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url


class Site(models.Model):
    """
    站点配置
    """
    desc = models.CharField(max_length=50, verbose_name='网站描述')
    keywords = models.CharField(max_length=50, verbose_name='网站关键词')
    title = models.CharField(max_length=50, verbose_name='网站标题')
    index_title = models.CharField(max_length=50, verbose_name='首页标题')
    type_chinese = models.CharField(max_length=50, verbose_name='座右铭汉语')
    type_english = models.CharField(max_length=80, verbose_name='座右铭英语')
    icp_number = models.CharField(max_length=20, verbose_name='备案号')
    icp_url = models.CharField(max_length=50, verbose_name='备案链接')
    site_mail = models.CharField(max_length=50, verbose_name='我的邮箱')
    site_qq = models.CharField(max_length=50, verbose_name='我的QQ')
    site_avatar = models.CharField(max_length=200, default='https://image.3001.net/images/20171226/15142933784705.png', verbose_name='我的头像')

    class Meta:
        verbose_name = '网站设置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
