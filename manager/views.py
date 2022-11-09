from django.shortcuts import render

# Create your views here.
def managerScreen(request):
    return render(request, 'html/managerScreen.html', {})