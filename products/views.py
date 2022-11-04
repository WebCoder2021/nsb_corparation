from django.shortcuts import render

# Create your views here.
def products(request):
    context = {}
    context['product'] = True
    return render(request,'shop.html',context)
def product_detail(request,id):
    context = {}
    context['product'] = True
    return render(request,'shop-details.html',context)
def product_cart(request):
    context = {}
    context['product'] = True
    return render(request,'shopping-cart.html',context)