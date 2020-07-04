from django.shortcuts import render
from django.http import HttpResponse
from .models import Shop,Shop_Product
from product_info.models import CategoryModel
from faker import Faker
# Create your views here.
def storeView(request, **kwargs):
    context = {
        "categories": CategoryModel.get(), "shopProducts": Shop_Product.get(kwargs['id'])
    }
    return render(request,template_name='storepage.html', context=context)

def script(request):

    shop = Shop.objects.all()
    sp = Shop_Product.objects.all()


    # print("shppd info")
    # for i in sp:
    #     print(i.shop)
    #     print(i.products.all())

    return HttpResponse(status=200)