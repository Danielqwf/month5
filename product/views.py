from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from . import models
from product.serializers import *
from rest_framework.decorators import api_view


@api_view(['GET'])
def category_list_api_view(request):
    if request.method == 'GET':
        categoryes = Category.objects.all()
        serializer = CategorySerializer(categoryes, many=True).data
        return Response(data=serializer)


@api_view(['GET'])
def category_detail_api_view(request, id):
    if request.method == 'GET':
        # category = get_object_or_404(models.Category, id=id)
        serializer = CategorySerializer(category, many=False).data
        return Response(data=serializer)


@api_view(['GET'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True).data
        return Response(data=serializer)


@api_view(['GET'])
def product_detail_api_view(request, id):
    if request.method == 'GET':
        product = get_object_or_404(Category, id=id)
        serializer = ProductSerializer(product, many=False).data
        return Response(data=serializer)


@api_view(['GET'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True).data
        return Response(data=serializer)


@api_view(['GET'])
def review_detail_api_view(request, id):
    if request.method == 'GET':
        review = get_object_or_404(Category, id=id)
        serializer = ReviewSerializer(review, many=False).data
        return Response(data=serializer)


@api_view(['GET'])
def products_review_api_view(request):
    queryset = Review.objects.all()
    data = ReviewSerializer(queryset, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)



