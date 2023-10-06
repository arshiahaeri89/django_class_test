from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'description']
    list_editable = ['price', 'is_active']
    prepopulated_fields = {'slug': ['title']}
    list_filter = ['is_active', 'price']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ['color', 'size']
    list_editable = ['size']


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['tag']


admin.site.register(Product, ProductAdmin)
admin.site.register(Karbaran)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductDetails, ProductDetailsAdmin)
admin.site.register(ProductTag, ProductTagAdmin)
