from django.contrib import admin
from product import models as mx


@admin.register(mx.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in mx.Category._meta.local_fields]


@admin.register(mx.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in mx.Product._meta.local_fields]


@admin.register(mx.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in mx.ProductImage._meta.local_fields]


@admin.register(mx.Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in mx.Specification._meta.local_fields]
