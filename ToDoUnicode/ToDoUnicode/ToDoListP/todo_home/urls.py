from django.contrib import admin
from django.urls import path
from . import views,views1

urlpatterns = [
    # path('', views.user, name= 'test'),
    # path('display/<int:id>', views.index, name = 'display_update'),
    # path('display/', views.index, name = 'dispaly'),
    # path('<int:id>/', views.display_todo, name = 'exist_display'),
    # path('update/<int:id>', views.update_data, name = 'user-update'),
    # path('display/delete/<int:id>/<str:task>', views.delete_data, name = 'user_delete')

    
    # path('', views1.login, name= 'login'),
    # path('register/', views1.register, name = 'registerurl'),
    path('display/<int:id>', views1.display, name = 'displayurl'),
    #path('display/', views1.display, name = 'display'),
    path('delete/<int:id>/<str:task>/<int:time>', views1.delete,name = 'deleteurl'),
    path('update/<int:pk>/<int:u_id>/<str:task>/<int:time>', views1.update, name = 'updateurl'),
    path('registerpage/',views1.registerpage, name ='registerpageurl'),
    path('loginpage/',views1.loginpage, name ='loginpageurl'),
    path('logout/',views1.logoutuser, name = 'logouturl'),

]
