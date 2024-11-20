from django.contrib import admin
from nested.admin import NestedCategoryAdmin
from .models import Product, Category, ProductImage


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


@admin.register(Category)
class CategoryAdmin(NestedCategoryAdmin):
    list_display = ('id', 'name') + NestedCategoryAdmin.list_display


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    change_list_template = "admin/nested/change_list.html"
