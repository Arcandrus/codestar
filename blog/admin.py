from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('author', 'post', 'created_on')
    search_fields = ['author__username', 'post__title']
    list_filter = ('approved', 'created_on')
    summernote_fields = ('content',)