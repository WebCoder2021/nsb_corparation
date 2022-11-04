
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home,name='home'),
    path('about', about,name='about'),
    path('blog', blog,name='blog'),
    path('blog/<int:id>/', blog_detail,name='blog_detail'),
    path('blog/<int:id>/', home,name='blog_detail'),
    path('contact', contact,name='contact'),
    path('checkout', checkout,name='checkout'),
    path('product/', include('products.urls')),
]
