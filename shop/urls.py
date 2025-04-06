from django.urls import path
from .views import AllProductsListView, ProductListView, ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('', AllProductsListView.as_view(), name='product_list'),  # <- ეს
    path('category/<slug:slug>/', ProductListView.as_view(), name='product_list_by_category'),
    path('', AllProductsListView.as_view(), name='all_products'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
]
