from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('add/', views.product_add, name='product_add'),
    path('<slug:slug>/', views.product_list_by_category, name='product_list_by_category'),
    path('<category_slug>/<product_slug>/', views.product_detail, name='product_detail'),
]
