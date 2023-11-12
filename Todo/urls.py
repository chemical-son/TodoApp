from django.urls import path

from . import views


app_name = "todo"
urlpatterns = [
    path("", views.get_todo_lists, name="get_todo_lists"),
    path("add/", views.add_todo, name="add_todo"),
    path("delete/<int:pk>/", views.delete_todo, name="delete_todo"),
    path("change/<int:pk>/", views.change_todo_tatus, name="change_todo_tatus"),
]
