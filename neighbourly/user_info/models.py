from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

# Create your models here.

# class Shopkeeper(User):
#     date=models.DateTimeField(auto_now=True)
#     mobileno = models.CharField(max_length=10)
#     def __str__(self):
#         return self.name

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


# class user_customer(models.Model):
#     # customer_user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     date=models.DateTimeField(auto_now=True)
#     mobileno = models.IntegerField(default=999999999)
#     add = models.CharField(max_length=1000)
    
# #     #above fields are builtin
# #     # stars = models.FloatField()
# #     # status = models.IntegerField(default=0)
    
#     def __str__(self):
#         return self.customer_user.username

