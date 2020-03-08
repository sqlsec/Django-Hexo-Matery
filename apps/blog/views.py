import random
import mistune
from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Links, Article



def global_setting(request):
    """
    将settings里面的变量 注册为全局变量
    """
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESCRIPTION,
        'SITE_KEY': settings.SECRET_KEY,
        'SITE_MAIL': settings.SITE_MAIL,
        'SITE_ICP': settings.SITE_ICP,
        'SITE_ICP_URL': settings.SITE_ICP_URL,
        'SITE_TITLE': settings.SITE_TITLE,
        'SITE_TYPE_CHINESE': settings.SITE_TYPE_CHINESE,
        'SITE_TYPE_ENGLISH': settings.SITE_TYPE_ENGLISH
    }


class Index(View):
    """
    首页展示
    """
    def get(self, request):
        all_articles = Article.objects.all().order_by('-add_time')
        top_articles = Article.objects.filter(is_recommend=1)

        # f首页分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 9, request=request)
        articles = p.page(page)

        return render(request, 'index.html', {
            'all_articles': articles,
            'top_articles': top_articles
        })


class Friends(View):
    """
    友链链接展示
    """
    def get(self, request):
        links = Links.objects.all()
        card_num = random.randint(1, 10)
        return render(request, 'friends.html', {
            'links': links,
            'card_num': card_num,
        })


class Detail(View):
    """
    文章详情页
    """
    def get(self, request, pk):
        article = Article.objects.get(id=int(pk))
        article.viewed()
        mk = mistune.Markdown()
        output = mk(article.content)

        return render(request, 'detail.html', {
            'article': article,
            'detail_html': output
        })
