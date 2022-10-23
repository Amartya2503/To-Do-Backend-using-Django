from unicodedata import category
from django.shortcuts import render,HttpResponse
from .forms import *
from .models import todo, T_user
# Create your views here.
def user(request):
    
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
            print(todo.objects.all())
            #x= todo.objects.all()
            for x in todo.objects.all():
                print(x.status, x.time, x.task )
            return render(request, 'home.html', {'form' : form, 'instance' : str(instance)})

    form= todo_data()
    x= T_user.objects.all()
    for i in x:
        print(i.id, i.name)
    return render(request, 'home.html', {'form': form})
