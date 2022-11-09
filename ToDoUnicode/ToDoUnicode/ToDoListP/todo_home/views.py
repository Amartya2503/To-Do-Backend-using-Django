from ssl import Purpose
from unicodedata import category
from django.shortcuts import render,HttpResponse,redirect 
from .forms import *
from .models import todo, T_user
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def user(request):
    if request.method == 'POST':
       u_form = user_select(request.POST)
       if u_form.is_valid():
        f_id = u_form.cleaned_data['id']
        f_name= u_form.cleaned_data['name']

        try:
            T_user.objects.filter(id = f_id).get
            print('sucess', todo.objects.filter(use_by_id =f_id) )
            instance1 = todo.objects.filter(use_by_id = f_id)
            return render(request, 'display.html', {'varid': f_id, 'varname': f_name,'form': todo_data(), 'instance': instance1})

        except ObjectDoesNotExist:

            if request.method == "GET":         
                return render(request , 'signup.html',  { 'varname': f_name,'create_form': create_user(),'varid' : f_id})
               
            # return render(request, 'home.html', {'create_form' : create_form}) 
     
            else:
                create_form = create_user()
                return render(request, 'signup.html', {'create_form' : create_form, 'varname' : f_name, 'varid' : f_id})

                               
    else:
        u_form = user_select()
        return render(request, 'home.html', {'u_form' : u_form} )

def index(request,id):

    flag = 1
    if flag == 1 :

        # return HttpResponse("this is the test page")
        if request.method == 'POST':

            try:
                T_user.objects.get(id = id)
                form= todo_data(request.POST)
                if form.is_valid():
                    
                    taskf = form.cleaned_data['task']
                    timef = form.cleaned_data['time']
                    categoryf = form.cleaned_data['category']
                    if form.cleaned_data['status'] == 'Complete' :
                        statusf = 'True'
                    else:
                        statusf = 'False'
                    instance = todo(use_by_id = id, task = taskf, time = timef, category = categoryf, status = statusf)
                    instance.save()
                    flag = 1
                    return redirect("")

            except ObjectDoesNotExist:
                form= todo_data()
                return render(request, 'display.html', {'form': form })
        else:
            form= todo_data()
            return render(request, 'display.html', {'form': form , 'instance' : todo.objects.filter(use_by_id = id)})
    else:
        form= todo_data()
        return render(request, 'display.html', {'form': form })
        

def update_data(request,id):
    instance = todo.objects.filter(use_by_id = id)
    return render(request, 'display.html', {'form': todo_data(instance), 'instance': instance})


def delete_data(request,id,task):
    instance = todo.objects.filter(use_by_id = id, task = task)
    print(instance)
    instance.delete()
    return redirect('')   
    



def display_todo(request, id):
    print("the id is :", id)
    print('sucess', todo.objects.filter(use_by_id = id) )#debugging Purpose
    context ={
        'varname': todo.objects.filter(use_by_id = id)

    }
    return render(request, 'display.html', context)

def login_user(request):
    if request.method == 'POST':
        print("nope")
