from django.urls import path
from . import views # where the period means this directory

urlpatterns = [
    path('', views.managerScreen, name="managerScreen"),
]