from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logoutPage, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('store/', views.store, name='store'),
    path('update_item/', views.updateItem, name='update_item')


]
