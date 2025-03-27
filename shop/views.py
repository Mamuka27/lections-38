from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Category, Product
from .forms import ProductForm 

class AllProductsListView(ListView):
    model = Product
    template_name = 'shop/all_products.html'
    context_object_name = 'products'

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Product,
            category__slug=self.kwargs['category_slug'],
            slug=self.kwargs['product_slug']
        )

class ProductCreateView(CreateView):
    model = Product
    template_name = 'shop/product_add.html'
    form_class = ProductForm 

    def get_success_url(self):
        return self.object.get_absolute_url()
