from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views # where the period means this directory

urlpatterns = [
    path('', views.loginScreen, name="loginScreen"),
] 

urlpatterns += staticfiles_urlpatterns()