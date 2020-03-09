import random
import datetime
import mistune
from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Links, Article, Category, Tag


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

        # 首页分页功能
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


class Archive(View):
    """
    文章归档
    """
    def get(self, request):
        all_articles = Article.objects.all().order_by('-add_time')
        all_date = all_articles.values('add_time')
        latest_date = all_date[0]['add_time']
        all_date_list = []
        for i in all_date:
            all_date_list.append(i['add_time'].strftime("%Y-%m-%d"))

        # 遍历1年的日期
        end = datetime.date(latest_date.year, latest_date.month, latest_date.day)
        begin = datetime.date(latest_date.year-1, latest_date.month, latest_date.day)
        d = begin
        date_list = []
        temp_list = []

        delta = datetime.timedelta(days=1)
        while d <= end:
            day = d.strftime("%Y-%m-%d")
            if day in all_date_list:
                temp_list.append(day)
                temp_list.append(all_date_list.count(day))
            else:
                temp_list.append(day)
                temp_list.append(0)
            d += delta
            date_list.append(temp_list)
            temp_list = []

        # 文章归档分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 10, request=request)
        articles = p.page(page)

        return render(request, 'archive.html', {
            'all_articles': articles,
            'date_list': date_list
        })
