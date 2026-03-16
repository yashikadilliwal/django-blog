from django.contrib import admin

# Register your models here.
from .models import Category, Blog  

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured', )
    search_fields = ('id', 'title', 'category__category_name', 'status',)
    list_editable = ('status', 'is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
