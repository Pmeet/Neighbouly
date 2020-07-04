from django.db import models

# Create your models here.
class Product(models.Model):

    pid = models.AutoField(primary_key=True, unique=True, verbose_name='Product ID')
    name = models.CharField(max_length=100, verbose_name='Name', null=False)
    price = models.IntegerField(default=0, verbose_name='Price', null=False)
    description = models.TextField(verbose_name='Description', null=False)
    image = models.ImageField(verbose_name='Product Image')
    expiry = models.CharField(max_length=100, verbose_name='Expiry (in months)', default='NA') 
    quantity = models.CharField(max_length=50, verbose_name='Quantity',null=True, default='NA')

    def __str__(self):
        return self.name

    @classmethod
    def get(cls):
        result = cls.objects.all()
        return_list = []
        for i in result.values_list():
            obj_dict = {}
            obj_dict['name'] = i[1]
            obj_dict['price'] = i[2]
            obj_dict['description'] = i[3]
            obj_dict['image'] = i[4]
            obj_dict['expiry'] = i[5]
            obj_dict['quantity'] = i[6]
            return_list.append(obj_dict)
        return return_list


class CategoryModel(models.Model):
    CATEGORIES = (
        ('Groceries','Groceries'), 
        ('Pharmacy','Pharmacy'), 
        ('Music', 'Music'),
        ('Pets',  'Pets'), 
        ('Sports', 'Sports'), 
        ('Flowers', 'Flowers'),
        ('Stationery', 'Stationery'), 
        ('Books', 'Books'), 
        ('Scientific Equipments', 'Scientific Equipments'),
        ('Health', 'Health'), 
        ('Fashion', 'Fashion'),
        ('Travel', 'Travel')
    )
    cid = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=100, verbose_name='Name', choices=CATEGORIES)

    def __str__(self):
        return self.name

    @classmethod
    def get(cls):
        result = cls.objects.all()
        return_list = []
        for i in result:
            return_list.append(i.name)
        return return_list    