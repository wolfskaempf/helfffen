from django.urls import path

from . import views

app_name = 'helfffen'
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:task_id>', views.task_show, name='task_show'),
]
