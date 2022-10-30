from django import forms 
from .models import T_user
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
    id = forms.IntegerField(label= 'Enter id :')
    name = forms.CharField( max_length=120, required=False)
    number =forms.IntegerField(label = 'phone.No:')
    email = forms.CharField(label = 'enter email', max_length = 120)