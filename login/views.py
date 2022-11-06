from django.shortcuts import render
from login.models import Inventory

# Create your views here.
def loginScreen(request):
    inventory_objs = Inventory.objects.all()
    context = {
        "inventory": inventory_objs
    }
    return render(request, 'html/loginScreen.html', context)