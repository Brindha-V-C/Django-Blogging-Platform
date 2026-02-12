from django.urls import path

from . import views

urlpatterns = [
    #Add Task
    path('addTask/', views.addTask, name='addTask'),

    #Mark task as done
    path('completed_task/<int:pk>/', views.completed_task, name='completed_task'),

    #Mark task as undone
    path('not_completed_task/<int:pk>', views.not_completed_task, name="not_completed_task"),

    #Edit task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    #Delete task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]