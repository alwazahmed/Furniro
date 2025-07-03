from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:furniture_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),


]
