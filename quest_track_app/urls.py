from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('create_task',views.create_task),
    path('task_creation', views.task_creation),
    path('delete/<int:id>', views.delete_task),
    path('edit_task/<int:id>', views.edit),
    path('update_task/<int:id>', views.update_task),
    path('all_tasks', views.all_tasks),
    path('complete_task/<int:id>', views.complete_task),
    path('view_task/<int:id>', views.view_task),
    path('task_completion/<int:id>', views.task_completion)

    
]