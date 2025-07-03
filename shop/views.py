from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404, redirect
from .models import Furniture, Cart, CartItem
from django.contrib.auth.decorators import login_required
from shop.models import Furniture
# Create your views here.
from django.views.decorators.http import require_POST

@login_required
def checkout_success(request):
    return render(request, 'shop/checkout_success.html')

@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(item.furniture.price * item.quantity for item in items)
    shipping = 200
    grand_total = total + shipping

    if request.method == 'POST':
        items.delete()  # Clear the cart
        return render(request, 'shop/checkout_success.html')

    return render(request, 'shop/checkout.html', {
        'items': items,
        'total': total,
        'shipping': shipping,
        'grand_total': grand_total,
    })

@login_required
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')
@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = sum(item.furniture.price * item.quantity for item in items)
    shipping = 50  # Fixed shipping cost
    GrandTotal = total + shipping  # Add shipping cost to total
    return render(request, 'shop/cart.html', {'items': items, 'total': total, 'GrandTotal': GrandTotal, 'shipping': shipping})

@login_required
def add_to_cart(request, furniture_id):
    furniture_item = get_object_or_404(Furniture, id=furniture_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, furniture=furniture_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

def home(request):
    furniture_items = Furniture.objects.all()  # Fetches all entries from the database
    return render(request, 'shop/home.html', {'furniture_items': furniture_items})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')