from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from .models import Article, Category, Tag, Comment, Links


# 文章
@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category', 'cover_data', 'is_recommend', 'add_time', 'update_time')
    search_fields = ('title', 'desc', 'content')
    list_filter = ('category', 'tag', 'add_time')
    list_editable = ('category', 'is_recommend')
    readonly_fields = ('cover_admin', )
    list_per_page = 15

    fieldsets = (
        ('编辑文章', {
            'fields': ('title', 'content')
        }),
        ('其他设置', {
            'classes': ('collapse', ),
            'fields': ('cover', 'cover_admin', 'desc', 'is_recommend', 'click_count', 'tag', 'category', 'add_time'),
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }


# 分类
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'index', 'active', 'get_items', 'icon', 'icon_data')
    search_fields = ('name', )
    list_editable = ('active', 'index', 'icon')
    readonly_fields = ('get_items',)


# 标签
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_items')
    search_fields = ('name', )
    readonly_fields = ('get_items',)
    list_per_page = 20


# 评论
@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('content', 'username', 'article')
    search_fields = ('content', 'username', 'article')
    list_display = ('add_time', )


# 友链
@admin.register(Links)
class LinksAdmin(ImportExportModelAdmin):
    list_display = ('title', 'url', 'avatar_data', 'desc')
    search_fields = ('title', 'url', 'desc')
    readonly_fields = ('avatar_admin', )
    list_editable = ('url',)

    fieldsets = (
        (None, {
            'fields': ('title', 'url', 'desc', 'avatar_admin', 'image', )
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }
