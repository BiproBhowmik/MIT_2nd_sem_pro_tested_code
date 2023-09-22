from . import views
from django.urls import include, path

urlpatterns = [
    path('emailPredict/', views.emailPredict),
]
