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



from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get_object(self):
        return get_object_or_404(Product, id=self.kwargs['id'])

class ProductCreateView(CreateView):
    model = Product
    template_name = 'shop/product_add.html'
    form_class = ProductForm

    def get_success_url(self):
        return self.object.get_absolute_url()


from .forms import ProductForm

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_add.html'
