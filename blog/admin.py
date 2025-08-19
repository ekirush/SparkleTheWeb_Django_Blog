from django.contrib import admin
from .models import UserProfile, Post, Comment, Rating, Page

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "slug")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}  # auto-fill slug
    list_filter = ("created_at", "author")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at")
    search_fields = ("content",)

class RatingAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "rating")

class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

# Register models with custom admins
admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Page, PageAdmin)

