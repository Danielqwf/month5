from django.contrib import admin

from django.contrib import admin
from .models import Product, Review, Category

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)