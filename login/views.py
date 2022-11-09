from django.shortcuts import render

# Create your views here.
def loginScreen(request):
    return render(request, 'html/loginScreen.html', {})