from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , LogoutView 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path( '' , views.task_list , name= 'task'),
    path('signup',views.signup_view,name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('addtask',views.add_task,name='addtask'),
    path('edittask/<int:task_id>',views.edit_task,name='edittask')

]