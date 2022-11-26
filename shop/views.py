from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


def product_list(request, category_slug=None):
    serializer_class = CategorySerializer, ProductSerializer
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products,
                      'serializer_class': serializer_class
                  })

