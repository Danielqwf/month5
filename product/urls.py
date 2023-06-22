from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/categories/', views.category_list_api_view, name='category_list'),
    path('api/v1/categories/<int:id>/', views.category_detail_api_view, name='category_detail'),
    path('api/v1/products/', views.product_list_api_view, name='product_list'),
    path('api/v1/products/<int:id>/', views.product_detail_api_view, name='product_list'),
    path('api/v1/reviews/', views.review_list_api_view, name='review_list'),
    path('api/v1/reviews/<int:id>/', views.review_detail_api_view, name='review_detail'),

]

