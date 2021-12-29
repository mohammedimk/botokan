from django.shortcuts import render
from account.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products

    }
    return render(request, 'product/home.html', context)
