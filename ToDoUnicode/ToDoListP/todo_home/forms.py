from django import forms 
from .models import T_user
# x= T_user.objects.all()
class todo_data(forms.Form):

    task = forms.CharField(label= "task desc", max_length=122)
    time = forms.IntegerField(label= "in hours")
    status = forms.ChoiceField(choices =[('complete','Complete'), ('pending','Pending')])
    category = forms.ChoiceField(choices=[('high','High'),('medium','Medium'),('low','Low')])

class user_select(forms.Form):
    
    id = forms.ChoiceField(choices= [('1','One')], label= 'id :')