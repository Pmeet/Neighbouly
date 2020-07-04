from django.shortcuts import render
from .models import CategoryModel,Product
from django.http import HttpResponse
from shop_info.models import Shop
# Create your views here.

def category(request, **kwargs):
    context = { "categories": CategoryModel.get(), "shops": Shop.get(kwargs['cat'])}
    return render(request,'category.html',context)

def script(request):
    return HttpResponse(status=200)
