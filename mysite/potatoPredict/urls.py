from . import views
from django.urls import include, path

urlpatterns = [
    path('pricePredict/', views.pricePredict),
]
