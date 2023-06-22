from django.db import models


class Category(models.Model):
    name = models.CharField(null=True, max_length=112)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=112)
    description = models.CharField(max_length=112)
    price = models.DecimalField(default=0, blank=True, max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, related_name='category_object')

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.TextField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')


