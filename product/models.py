from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(null=True, max_length=112)

    @property
    def products_count(self):
        return self.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(default=0, blank=True, max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_object')

    def __str__(self):
        return self.title


STARS = (
    (1, '*'),
    (2, 2 * ' * '),
    (3, 3 * ' * '),
    (4, 4 * ' * '),
    (5, 5 * ' * '),
)


class Review(models.Model):
    title = models.TextField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')
    rating = models.PositiveIntegerField(null=True, blank=True, choices=STARS)





