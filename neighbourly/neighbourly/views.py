from django.shortcuts import render
from product_info.models import CategoryModel

def index(request):
    context = {
        "categories":CategoryModel.get()
    }
    return render(request,'Home.html',context=context)