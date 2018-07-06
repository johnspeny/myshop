from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
# Create your views here.

@require_POST
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	forms = CartAddProductForm(request.POST)
	if forms.is_valid():
		cd = forms.cleaned_data
		cart.add(product,cd['quantity'],cd['update'])
	return redirect('cart:cart_detail')

def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/detail.html', context)