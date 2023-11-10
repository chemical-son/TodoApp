from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include("authentication.urls")),
    path('todo/', include("Todo.urls")),
    path('admin/', admin.site.urls),
]
