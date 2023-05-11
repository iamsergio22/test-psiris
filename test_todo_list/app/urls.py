from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("insert",views.insert,name="insert"),
    path("delete/<int:task_id>",views.delete,name="delete"),
    path("update/<int:task_id>",views.update_form,name="update_form"),
    path("update",views.update,name="update"),
    path("update/completed/<int:task_id>",views.update_completed,name="update_completed"),
    path("completed",views.tasks_completed,name="tasks_completed"),
]