from django.shortcuts import render , redirect
from django.contrib import messages
# Create your views here.


def signin(request):
    if request.method == 'POST' and 'btn_login' in request.POST:

        messages.info(request,'test and btn_login')

        return redirect('signin')
    else:
        return render(request , 'signin.html')
    


def signup(request):
    if request.method == 'POST' and 'btn_signup' in request.POST:
        messages.info(request,'test and btn_signup')
        return redirect('signup')
    else:
        return render(request , 'signup.html')
    


def profile(request):
    if request.method == 'POST' and 'btn_save' in request.POST:
        messages.info(request,'test and btn_save')
        return redirect('profile')
    else:
        return render(request , 'profile.html')
    