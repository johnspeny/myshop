from django.shortcuts import render, get_object_or_404
import cart.forms as form
from .models import Category, Product
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.


def index(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    c = ContactForm()
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        sender = request.POST.get('sender', '')
        forms = ContactForm(request.POST)
        if forms.is_valid():
            send_mail(subject, message, sender, ['johnspeny@gmail.com'],fail_silently=False,)
            c = ContactForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {'categories': categories, 'products': products, 'f':c}

    return render(request, 'shop/index.html', context)


def detail(request, id, slug):
    forms = form.CartAddProductForm()
    product = Product.objects.get(id=id, slug=slug) or get_object_or_404(Product, id=id, slug=slug)
    context = {'products': product, 'form': forms}
    return render(request, 'shop/detail.html', context)