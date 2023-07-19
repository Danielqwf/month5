from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/categories/', views.CategoryView.as_view({'get':'list', 'post':'create'})),
    path('api/v1/categories/<int:pk>/', views.CategoryView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('api/v1/products/', views.ProductView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/products/<int:pk>/', views.ProductView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('api/v1/reviews/', views.ReviewView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/reviews/<int:pk>/', views.ReviewView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='review_detail'),
    path('api/v1/products/reviews/', views.products_review_api_view, name='products_review'),
]
