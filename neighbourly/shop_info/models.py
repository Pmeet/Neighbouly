from django.db import models
from product_info.models import Product,CategoryModel

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=150,verbose_name='Name')
    address = models.TextField(max_length=400,verbose_name="Address")
    image = models.ImageField(verbose_name='Shop Image')
    belongs_to_category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    # get latitude and longitude based on address using geolocation-python module

    def __str__(self):
        return self.name

    @classmethod
    def get(cls,category=None):
        if category is not None:
            result = cls.objects.filter(belongs_to_category__name=category)
            return_list=[]
            for i in result.values():
                return_list.append(i)
            print(return_list)
            return return_list
        else:
            result = cls.objects.all()
            return_list=[]
            for i in result.values():
                return_list.append(i)
            return return_list

class Shop_Product(models.Model):
    name = models.CharField(max_length=150,verbose_name='Name',default='list')
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

    @classmethod
    def get(cls,id):
        q1 = cls.objects.filter(shop=id)
        return_list=[]
        for i in q1:
            q2 = i.products.all()
            for i in q2.values():
                return_list.append(i)
        return return_list 

    
    
