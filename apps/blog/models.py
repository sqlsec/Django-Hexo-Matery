from django.db import models


class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(max_length=30, verbose_name='标签名称')

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=99, verbose_name='分类排序')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='文章分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')

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
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content[:20]


class Links(models.Model):
    """
    友情链接
    """
    title = models.CharField(max_length=50, verbose_name='友情链接标题')
    url = models.URLField(verbose_name='友情链接地址')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '友情链接'
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

    class Meta:
        verbose_name = '网站设置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
