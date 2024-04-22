from django.shortcuts import render
from . models import *


# Create your views here.
def home(request):
      context = {}
      return render(request, 'cars/home.html', context)

def base(request):
      context = {}
      return render(request, 'cars/base.html', context)

def blog(request):
     context = {}
     return render(request, 'cars/blog.html', context)

def about(request):
      staff= Staff.objects.all()
      context = {"staff":staff} 

      return render(request, 'cars/about.html', context)

def contact(request):
      context = {}
      return render(request, 'cars/contact.html', context)

def faq(request):
      context = {}
      return render(request, 'cars/faq.html', context)

def page(request):
      context = {}
      return render(request, 'cars/page.html', context)




