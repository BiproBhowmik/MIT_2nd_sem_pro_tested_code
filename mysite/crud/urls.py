from . import views
from django.urls import include, path

urlpatterns = [
    path('read/', views.read),
    path('create/', views.create),
    path('update/', views.update),
    path('delete/', views.delete),
]
