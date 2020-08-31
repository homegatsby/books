from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id','title', 'category', 'created_at', 'get_image')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'get_image',)
    fields = ('title', 'slug', 'category', 'tags', 'description', 'created_at', 'image', 'get_image',)
    list_display_links = ('id', 'title',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50"')
        return '-'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Book, BookAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
