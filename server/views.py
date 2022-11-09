# Create your views here.
from django.shortcuts import render

# Create your views here.
def serverScreen(request):
    return render(request, 'html/serverScreen.html', {})