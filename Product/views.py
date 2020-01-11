from django.shortcuts import render
from Product.models import Product
from cart.forms import CartAddProductForm
# Create your views here.

def index(request):
    lstProducts = Product.objects.all()
    return render(request, 'Product/index.html', {'lsProducts': lstProducts})

def product_detail(request, id):
    product = Product.objects.get(id = id)
    cart_product_form = CartAddProductForm()
    return render(request, 'Product/product-detail.html', {'product': product, 'cart_product_form': cart_product_form})
