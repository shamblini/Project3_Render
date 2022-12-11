from  django.urls  import  path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views 

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('social/signup/', views.signup_redirect, name='signup_redirect'),
]
# urlpatterns += staticfiles_urlpatterns()