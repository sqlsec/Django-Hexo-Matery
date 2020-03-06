from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from .models import Article, Category, Tag, Comment, Links


# 文章
@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category', 'cover_data', 'is_recommend')
    search_fields = ('title', 'desc', 'content')
    list_filter = ('category', 'tag', 'add_time')
    list_editable = ('category', 'is_recommend')
    readonly_fields = ('cover_admin', )

    fieldsets = (
        ('编辑文章', {
            'fields': ('title', 'content')
        }),
        ('其他设置', {
            'classes': ('collapse', ),
            'fields': ('cover', 'cover_admin', 'desc', 'is_recommend', 'click_count', 'tag', 'category', 'add_time'),
        }),
    )


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
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('content', 'username', 'article')
    search_fields = ('content', 'username', 'article')
    list_display = ('add_time', )


# 友链
@admin.register(Links)
class LinksAdmin(ImportExportModelAdmin):
    list_display = ('title', 'url', 'avatar_data')
    search_fields = ('title', 'url')
    readonly_fields = ('avatar_admin', )

    fieldsets = (
        (None, {
            'fields': ('title', 'url', 'image', 'avatar_admin')
        }),
    )
