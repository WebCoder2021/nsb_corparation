
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', products,name='product'),
    path('<int:id>/detail', product_detail,name='product_detail'),
    path('cart/', product_cart,name='product_cart'),
]
