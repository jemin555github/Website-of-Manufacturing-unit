from django.shortcuts import render
from .models import *


def home(request):
    sliders =Slider.objects.all()
    context={'sliders':sliders}
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html')


def product(request):
    return render(request,'product.html')


def capabilities(request):
    return render(request,'capabilities.html')


def quality(request):
    return render(request,'quality.html')


def contact(request):
    return render(request,'contact.html')


# Create your views here.
