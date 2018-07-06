from django.shortcuts import render
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import OrderItem
from django.core.mail import send_mail
# Create your views here.
def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			send_mail(
    					'Your order awaits you',
    					'Thank you for placing your order.Come to the pick up station',
    					'okkerjohn@gmail.com',
    					['johnspeny@gmail.com'],
    					fail_silently=False,
					)
			for item in cart:
				OrderItem.objects.create(order=order,
					product=item['product'],price=item['price'],quantity=item['quantity'])
			cart.clear()
		return render(request, 'orders/created.html',{'order':order})
	else:
		form = OrderCreateForm()

	context = {'cart':cart,'form':form}
	return render(request, 'orders/create.html',context)
