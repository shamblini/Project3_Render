from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views # where the period means this directory

urlpatterns = [
    path('', views.managerScreen, name="managerScreen"),

    path('analytics/', views.analytics, name="analytics"),

    path('products/', views.getProducts, name="get-products"),
    path('products/change/<id>', views.showProduct, name="show-product"),
    path('products/add/', views.addProduct, name="add-product"),
    path('products/change/delete/<id>', views.deleteProduct, name="delete-product"),

    path('categories/', views.getCategories, name="get-categories"),
    path('categories/change/<id>', views.showCategory, name="show-category"),
    path('categories/add/', views.addCategory, name="add-category"),
    path('categories/change/delete/<id>', views.deleteCategory, name="delete-category"),

    path('transactions/', views.getTransactions, name="get-transactions"),
    path('transactions/change/<id>', views.showTransaction, name="show-transaction"),
    path('transactions/add/', views.addTransaction, name="add-transaction"),
    path('transactions/change/delete/<id>', views.deleteTransaction, name="delete-transaction"),

    path('employees/', views.getEmployees, name="get-employees"),
    path('employees/change/<id>', views.showEmployee, name="show-employee"),
    path('employees/add/', views.addEmployee, name="add-employee"),
    path('employees/change/delete/<id>', views.deleteEmployee, name="delete-employee"),

    path('recipes/', views.getRecipes, name="get-recipes"),
    path('recipes/change/<id>', views.showRecipe, name="show-recipe"),
    path('recipes/add/', views.addRecipe, name="add-recipe"),
    path('recipes/change/delete/<id>', views.deleteRecipe, name="delete-recipe"),

    path('jobs/', views.getJobs, name="get-jobs"),
    path('jobs/change/<id>', views.showJob, name="show-job"),
    path('jobs/add/', views.addJob, name="add-job"),
    path('jobs/change/delete/<id>', views.deleteJob, name="delete-job"),

    path('customers/', views.getCustomers, name="get-customers"),
    path('customers/change/<id>', views.showCustomer, name="show-customer"),
    path('customers/add/', views.addCustomer, name="add-customer"),
    path('customers/change/delete/<id>', views.deleteCustomer, name="delete-customer"),
]