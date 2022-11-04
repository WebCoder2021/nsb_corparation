from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    context['home'] = True
    return render(request,'index.html',context)
def about(request):
    context = {}
    context['about'] = True
    return render(request,'about.html',context)
def blog(request):
    context = {}
    context['blog'] = True
    return render(request,'blog.html',context)
def blog_detail(request,id):
    context = {}
    context['blog'] = True
    return render(request,'blog-details.html',context)
def contact(request):
    context = {}
    context['contact'] = True
    return render(request,'contact.html',context)
def checkout(request):
    context = {}
    context['product'] = True
    return render(request,'checkout.html',context)