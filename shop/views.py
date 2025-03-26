# shop/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import ProductForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})

def product_list_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all() 
    return render(request, 'shop/product_list.html', {
        'category': category,
        'products': products
    })

def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug, category=category)
    return render(request, 'shop/product_detail.html', {
        'category': category,
        'product': product
    })

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('shop:product_detail', category_slug=product.category.slug, product_slug=product.slug)
    else:
        form = ProductForm()
    return render(request, 'shop/product_add.html', {'form': form})
