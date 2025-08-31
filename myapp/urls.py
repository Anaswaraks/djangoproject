from django.urls import path
from . import views


urlpatterns = [
    path('name/',view=views.name,name='name'),
    path('display/',view=views.display,name='display'),
    path('students/',view=views.students,name='students'),
    path('students/student/<int:id>',view=views.one_student,name='one_student'),
   
    path('login/',view=views.login,name='login'),
    path('register/',view=views.register,name='register'),
    path('',views.homepage,name='homepage'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('user_logout/',view=views.user_logout,name='user_logout'),
    
    #API
    path('api/getuser/',views.get_user,name='get_user'),
    path('api/getuser/createuser/', views.create_user,name='create_user'),
    path('api/getusersdb/',views.get_users_db,name='get_users_db'),
    
    ]
