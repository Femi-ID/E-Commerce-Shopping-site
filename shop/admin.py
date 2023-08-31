from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin
# Register your models here.


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']

    def get_prepopulated_fields(self, requst, obj=None):
        return {'slug': ('name',)}


"""django-parler integrates smoothly with the Django administration site. 
It includes a TranslatableAdmin class that overrides the ModelAdmin class provided by Django to manage model translations.
It doesn't support the prepopulated_fields attribute, but supports the get_prepopulated_ fields() method that provides the same functionality
"""

# command to create a new migration for the model translations:
# python manage.py makemigrations shop --name "translations"

# this migration deletes the previous existing fields from your models. This means that you will lose that data
# and will need to set your categories and products again in the administration site after running it

