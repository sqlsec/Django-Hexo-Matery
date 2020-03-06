from django.contrib import admin
from django.urls import path, re_path, include

from blog.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index')
]

# 设置后台名称
admin.site.site_header = '国光博客后台'
admin.site.site_title = 'Django Blog 后台'