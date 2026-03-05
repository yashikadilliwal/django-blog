from django.contrib import admin

# Register your models here.
from .models import Category, Blog  

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
