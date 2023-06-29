from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from . import models
from product.serializers import *
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categoryes = Category.objects.all()
        data = CategorySerializer(categoryes, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        serializer = CategorySerializer(category, many=False).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, many=False).data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        category.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product, many=False).data
        return Response(data=serializer)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, many=False).data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False).data
        return Response(data=serializer)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, many=False).data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def products_review_api_view(request):
    queryset = Review.objects.all()
    data = ReviewSerializer(queryset, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)
