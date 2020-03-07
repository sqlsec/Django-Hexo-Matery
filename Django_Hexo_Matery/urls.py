from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from blog.views import Index, Friends

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    # 友情链接
    path('friends/', Friends.as_view(), name='friends'),
    # 后台 markdown 编辑器配置
    path('mdeditor/', include('mdeditor.urls')),
]

# 设置后台名称
admin.site.site_header = '国光博客后台'
admin.site.site_title = 'Django Blog 后台'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)