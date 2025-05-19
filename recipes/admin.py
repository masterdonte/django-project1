from django.contrib import admin
from .models import Category, Recipe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # ...
    list_display = [field.name for field in Category._meta.fields]


admin.site.register(Category, CategoryAdmin)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Recipe._meta.fields]
    list_display = ('id', 'title', 'slug', 'created_at', 'is_published', 'cover', 'category', 'author')
