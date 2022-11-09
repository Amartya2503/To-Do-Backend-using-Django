from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import T_user
from .models import *
# x= T_user.objects.all()
class todo_data(forms.Form):

    task = forms.CharField(label= "task desc", max_length=122)
    time = forms.IntegerField(label= "in hours")
    status = forms.ChoiceField(choices =[('complete','Complete'), ('pending','Pending')])
    category = forms.ChoiceField(choices=[('high','High'),('medium','Medium'),('low','Low')])

class user_select(forms.Form):
    
    id = forms.IntegerField(label= 'Enter id :')
    name = forms.CharField( max_length=120, required=False)

class create_user(forms.Form):
    
    name = forms.CharField( max_length=120, required=False)
    id = forms.IntegerField(label= 'Enter id :')
    number =forms.IntegerField(label = 'phone.No:')
    email = forms.CharField(label = 'enter email', max_length = 120)

class usercreationform(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']


class loginuser(forms.Form):

    username = forms.CharField(label='Username:', max_length=120, required=False)
    password= forms.CharField(label= 'Enter password :')
    