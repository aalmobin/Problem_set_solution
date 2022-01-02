from django.contrib import admin
from .models import Variant, Product, ProductVariant, ProductImage, ProductVariantPrice


admin.site.register([Variant, Product, ProductVariant, ProductImage, ProductVariantPrice])
