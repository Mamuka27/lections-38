from django.urls import path
from .views import (
    AllProductsListView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
)

app_name = 'shop'

urlpatterns = [
    path('', AllProductsListView.as_view(), name='all_products'),  
    path('category/<slug:slug>/', ProductListView.as_view(), name='product_list_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
]
