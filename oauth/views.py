from django.shortcuts import render
# from django.shortcuts import redirect
# from django.contrib import messages

def homepage(request):
    return render(request=request, template_name= 'home.html',)

# def signup_redirect(request):
#     messages.error(request, "Something wrong here, it may be that you already have account!")
#     return redirect('homepage')