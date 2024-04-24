from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginuser, name='login'),
    path('home', views.home,name='home'),
    path('regform', views.register, name='reg'),
    path('todolist', views.Todolist.as_view(),name='listtodo'),
    path('projectlist', views.Projectlist.as_view() , name='listproject'),
    path('todoupdate/<int:pk>', views.TodoUp.as_view(), name='updatetodo'),
    path('todocreate',views.TodoCreate.as_view(),name='createtodo'),
    path('projectcreate',views.ProjectCreate.as_view(),name='createproject'),
    path('tododelete/<int:pk>', views.TodoDelt.as_view(), name='deletetodo'),
    path('home1', views.home1, name='home1'),
    path('projectupdate/<int:pk>',views.ProjectUpdate.as_view(),name='updateproject'),
    path('viewproject',views.Projectlist2.as_view(),name='viewproject'),
    path('projects/<int:project_id>/', views.project_details, name='project_details'),
    path('logout',views.logoutuser,name='logout'),
    path('deleteproject/<int:pk>',views.ProjectDelt.as_view(),name='deleteproject')
]
