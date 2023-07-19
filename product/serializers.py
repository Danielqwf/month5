from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=112)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    title = models.CharField(max_length=50)

    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Review
        fields = '__all__'


