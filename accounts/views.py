from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def signin(request):
    if request.GET:
        messages.info(request, 'Test Message1')
        messages.success(request, 'Test Message1')
        messages.error(request, 'Test Message1')

    return render(request , 'signin.html')
    


def signup(request):
    if request.POST:
        messages.info(request, 'This is post')

    if request.GET:
        messages.info(request, 'This is get')


    return render(request , 'signup.html')
    


def profile(request):
    return render(request , 'profile.html')
    