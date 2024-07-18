from django.urls import path
from .views import index, CategoryListCreate, CategoryDetail, ProductListCreate, ProductDetail

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]


