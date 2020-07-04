from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from .models import Shopkeeper

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','first_name','last_name','email','password1','password2')
        model = get_user_model()

    # as we used inbuilt from django and if we want to change the label of fields below is what you can do
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

# class ShopKeeperForm(forms.ModelForm):
#     class Meta:
#         model = Shopkeeper