from django.contrib import admin
from django.urls import include, path

from crud import views
from . import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),

    path('crud/', include('crud.urls')),
    path('accounts/', include('accounts.urls')),
    path('gpt/', include('gpt.urls')),
    path('potatoPredict/', include('potatoPredict.urls')),
    path('spamHam/', include('spamHam.urls')),
]
