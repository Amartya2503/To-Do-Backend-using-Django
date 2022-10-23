from unicodedata import category
from django.shortcuts import render,HttpResponse
from .forms import *
from .models import todo, T_user
# from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def user(request):
    if request.method == 'POST':
        form = user_select(request.POST)
        if form.is_valid():
            id_f = form.cleaned_data['id']
            try:
                instance = T_user.objects.get(id = id_f)

                context = {
                    # 'var1' : instance.name,
                    'u_form' : u_form
                    
                }
                print(instance.name)
                return render(request, 'home.html', context)

            except :
                return HttpResponse("not found ")
                
                                
    
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
            return render(request, 'display.html', {'form' : form, 'instance' : str(instance)})

    form= todo_data()
    # x= todo.objects.all()
    # for i in x :
    #     print(i.use_by.id)
    # print(str(x))
    x= T_user.objects.get(id = 2)
    print(x.name)
    return render(request, 'display.html', {'form': form})
