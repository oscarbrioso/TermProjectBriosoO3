#core/admin.py 

from django.contrib import admin
from core.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)