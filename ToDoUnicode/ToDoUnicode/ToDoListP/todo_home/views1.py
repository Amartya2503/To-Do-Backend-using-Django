from ssl import Purpose
from unicodedata import category
from django.shortcuts import render,HttpResponse,redirect 
from .forms import *
from .models import todo, T_user
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)
        user= authenticate(username = username, password = password)
        if user is not None:
            print(1, user.id)
            login(request, user)
            return redirect('displayurl', user.id) #3 is a variable here have to change in future 
        else:
            form = loginuser()
            return render(request, 'login.html', {'form':form, 'message': "username or password is incorrect please try again"})
    form = loginuser()
    return render(request, 'login.html', {'form':form})


def registerpage(request):
    if request.method == 'POST':
        form = usercreationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpageurl')
    form = usercreationform()
    return render(request,'signup.html', {'form':form})



@login_required(login_url ='/home/loginpage')
def display(request, id):
    if request.method == 'POST':
        form = todo_data(request.POST)
        if form.is_valid():
            taskf = form.cleaned_data['task']
            taskf = form.cleaned_data['task']
            timef = form.cleaned_data['time']
            categoryf = form.cleaned_data['category']
            if form.cleaned_data['status'] == 'Complete' :
                statusf = 'True'
            else:
                statusf = 'False'
            instance = todo(user_id= id, task = taskf, time = timef, category = categoryf, status = statusf)
            instance.save()
            return redirect('displayurl', id)
        
    instance1 = todo.objects.filter(user_id = id)
    return render(request, 'display.html', {'varid': id,'form': todo_data(), 'instance': instance1 })

@login_required(login_url ='/home/loginpage')
def delete(request,id,task,time):
    instance =todo.objects.filter(user_id = id, task = task, time = time)
    
    instance.delete()
    return redirect('displayurl', id)

@login_required(login_url ='/home/loginpage')
def update(request,pk,u_id,task,time):
    if request.method == 'POST':
        form  = todo_data(request.POST, initial={'task':task, 'time':time})
        if form.is_valid():
            taskf = form.cleaned_data['task']
            taskf = form.cleaned_data['task']
            timef = form.cleaned_data['time']
            categoryf = form.cleaned_data['category']
            if form.cleaned_data['status'] == 'Complete' :
                statusf = 'True'
            else:
                statusf = 'False'
            instance = todo(id = pk, user_id = u_id, task = taskf, time = timef, category = categoryf, status = statusf)
            instance.save()
            return redirect('displayurl', u_id)

    update = todo.objects.filter(user_id = u_id, task = task, time = time)
    print(update)
    form = todo_data(initial ={'task':task, 'time':time})
    return render(request, 'update.html',{'form': form,'varid':id})




@login_required(login_url ='/home/loginpage')
def logoutuser(request):
    logout(request)
    return redirect('loginpageurl')




# def login(request):
#     if request.method == 'POST':
#         form = user_select(request.POST)
#         if form.is_valid():
#             f_id = form.cleaned_data['id']
#             f_name= form.cleaned_data['name']
#             try:
#                 T_user.objects.get(id = f_id)
#                 instance1 = todo.objects.filter(use_by_id = f_id)
#                 return redirect('displayurl' , f_id)
#             except ObjectDoesNotExist:
#                 return redirect('register/')
    
#     form = user_select()
#     return render(request,'login.html', {'form':form} )

# def register(request):
#     if request.method == 'POST':
#         form = create_user(request.POST)
#         if form.is_valid():
                            
#             f_name = form.cleaned_data['name']
#             f_id = form.cleaned_data['id']
#             f_number = form.cleaned_data['number']
#             f_email = form.cleaned_data['email']
#             instance = T_user(name = f_name, id = f_id, number =f_number, email = f_email)
#             instance.save()
#             return redirect('/home/')

#     form = create_user()
#     return render(request,'signup.html', {'form':form})
