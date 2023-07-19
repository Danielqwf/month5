from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from product.serializers import *
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Category, Product, Review




class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@api_view(['GET'])
def products_review_api_view(request):
    queryset = Review.objects.all()
    data = ReviewSerializer(queryset, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)










