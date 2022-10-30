from ssl import Purpose
from unicodedata import category
from django.shortcuts import render,HttpResponse,redirect 
from .forms import *
from .models import todo, T_user
from django.urls import reverse
# from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def user(request):
    if request.method == 'POST':
       u_form = user_select(request.POST)
       if u_form.is_valid():
        
        f_id = u_form.cleaned_data['id']
        f_name= u_form.cleaned_data['name']
        try:
            T_user.objects.filter(id = f_id).get()
            print('sucess', todo.objects.filter(use_by_id =f_id) )
            instance1 = todo.objects.filter(use_by_id = f_id)
            return render(request, 'display.html', {'varid': f_id, 'varname': f_name,'form': todo_data(), 'instance': instance1})

        except:

            if request.method == "GET":

                create_form = create_user()
                return render(request, 'home.html', {'create_form' : create_form})

            else:

                create_form =create_user(request.POST)
                if create_form.is_valid():

                    f_id = create_form.cleaned_data['id']
                    f_name = create_form.cleaned_data['name']
                    f_num = create_form.cleaned_data['number']
                    f_email = create_form.cleaned_data['email']
                    instance = T_user(id =f_id, name = f_name , number = f_num, email =f_email)
                    instance.save()

                return render(request , 'signup.html',  { 'varname': f_name,'create_form': create_user()})
            # return render(request, 'home.html', {'create_form' : create_form})                                
    else:
        u_form = user_select()
        return render(request, 'home.html', {'u_form' : u_form} )

def index(request):
    # return HttpResponse("this is the test page")
    if request.method == 'POST':

        form= todo_data(request.POST)
        if form.is_valid():
            taskf = form.cleaned_data['task']
            timef = form.cleaned_data['time']
            categoryf = form.cleaned_data['category']
            if form.cleaned_data['status'] == 'Complete' :
                statusf = 'True'
            else:
                statusf = 'False'
            instance = todo( task = taskf, time = timef, category = categoryf, status = statusf)
            instance.save()
             
            
            return render(request, 'display.html', {'form' : form, 'instance' : todo.objects.filter(id= 3)})

    form= todo_data()
    # x= todo.objects.get(id = 2)

    # print(x.name)
    return render(request, 'display.html', {'form': form,'instance' : todo.objects.all() })

def create_data(id,task,time,category):
    instance= todo(id =id, task =task, time= time, category =category)
    instance.save()

def display_todo(request, id):
    print("the id is :", id)
    print('sucess', todo.objects.filter(use_by_id = id) )#debugging Purpose
    return HttpResponse('the id is <int:id>:',id)