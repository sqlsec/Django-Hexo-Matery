from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from .models import Article, Category, Tag, Comment, Links


# 文章
@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category', 'cover')
    search_fields = ('title', 'desc', 'content')
    list_filter = ('category', 'tag', 'add_time')


# 分类
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'index')
    search_fields = ('name', )


# 标签
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


# 评论
@admin.register(Comment)
class CommentAdmin(ImportExportActionModelAdmin):
    list_display = ('content', 'username', 'article')
    search_fields = ('content', 'username', 'article')
    list_display = ('add_time', )


# 友链
@admin.register(Links)
class LinksAdmin(ImportExportActionModelAdmin):
    list_display = ('title', 'url', 'image')
    search_fields = ('title', 'url')

