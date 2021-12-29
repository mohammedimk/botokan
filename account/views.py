from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import Product, Order, OrderItem, ShippingAddress
#from .forms import RegisterUserForm

# Create your views here.
#
# def register_user(request):
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password =

def store(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'account/store.html', context)


def cart(request):

    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order_items = order.orderitem_set.all()
        number_of_cart_items = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        number_of_cart_items = order['get_cart_items']

    context = {
        'order': order,
        'number_of_cart_items': number_of_cart_items,
        'order_items': order_items,
        'title': 'cart'
    }

    return render(request, 'account/cart.html', context)


def updateItem(request):

    data = json.loads(request.body)

    productId = data['productId']
    action = data['action']

    print('product', productId)
    print('action', action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return render(request, 'account/update.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')

        user1 = authenticate(username=username, password=password1)
        if user1 is not None:
            login(request, user1)
            return redirect('store')

        else:
            messages.info(request, "invalid Credentials")
            return redirect('login')

    context = {
        'title': 'login'
    }
    return render(request, 'account/login.html', context)


def registerPage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phone-number')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmation')

        if User.objects.filter(email=email).exists():
            messages.error(request, "the email is Already taken")
            return redirect('register')

        elif password1 != password2:
            messages.warning(request, "Your Password Does not match.")
            return redirect('register')

        user1 = User.objects.create_user(username=username, email=email, first_name=phoneNumber, password=password1)
        user1.save()
        messages.success(request, 'You have successfully Registered')
        return redirect('login')

    context = {

    }

    return render(request, 'account/register.html', context)


def profile(request):
    context = {

    }
    return render(request, 'account/profile.html', context)


def logoutPage(request):

    logout(request)

    context = {

    }
    return render(request, 'account/logout.html', context)


def contact(request):
    context = {

    }
    return render(request, 'account/contact.html', context)


