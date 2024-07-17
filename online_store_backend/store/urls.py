# store/urls.py
from django.urls import path
from .views import CategoryListCreate, CategoryDetail, ProductListCreate, ProductDetail
from . import views
from .views import index
from .views import IndexView


urlpatterns = [
    path('', views.index, name='index'),
    path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('<path:path>', IndexView.as_view(), name='catch_all'),
    path('api/categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]


