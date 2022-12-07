from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views # where the period means this directory
# switch sauce and cheese paths for sprint 2
urlpatterns = [
    path('', views.customerScreen, name="customerScreen"),
    path('Crust_selection/', views.Crust_selection, name="Cheese_selection"),
    path('Crust_selection/Cheese_selection/', views.Cheese_selection, name="Cheese_selection"),
    path('Crust_selection/Cheese_selection/Sauce_selection/', views.Sauce_selection, name="Sauce_selection"),
    path('Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/', views.Toppings_selection, name="Toppings_selection"),
    path('Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/Drizzle_selection/', views.Drizzle_selection, name="Drizzle_selection"),
    path('Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/Drizzle_selection/Checkout/', views.Checkout, name="Checkout"),
    
    
]

urlpatterns += staticfiles_urlpatterns()
