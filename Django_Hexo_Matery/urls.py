from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from blog.views import Index, Friends, Detail, Archive, Category_List

urlpatterns = [
    path('admin/', admin.site.urls),

    # 首页
    path('', Index.as_view(), name='index'),

    # 友情链接
    path('friends/', Friends.as_view(), name='friends'),

    # 后台 markdown 编辑器配置
    path('mdeditor/', include('mdeditor.urls')),

    # 文章详情
    re_path(r'article/av(?P<pk>\d+)', Detail.as_view(), name='detail'),

    # 文章归档
    path('article/', Archive.as_view(), name='archive'),

    # 分类统计
    path(r'category/', Category_List.as_view(), name='category')
]

# 设置后台名称
admin.site.site_header = '国光博客后台'
admin.site.site_title = 'Django Blog 后台'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)