from django.contrib import admin
from .models import Product, Category, Compagny, ProductSize, ProductSite, Comment
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')

admin.site.register(Category)
admin.site.register(Compagny)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Comment)

admin.site.site_header = "Product Review Admin"