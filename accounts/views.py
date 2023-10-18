from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
import re
# Create your views here.


def signin(request):
    if request.method == 'POST' and 'btn_login' in request.POST:

        username = request.POST['user']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)

        if user is not None :
            auth.login(request,user)
            messages.success(request, 'you are successfully logged in')
        else :
            messages.error(request, 'Username Or Password Invalid')

        return redirect('signin')
    else:
        return render(request , 'signin.html')


def signup(request):
    if request.method == 'POST' and 'btn_signup' in request.POST:

        # variables for Fields
        first_name = None
        last_name = None
        address = None
        address2 = None
        city = None
        state = None
        zip_number = None
        email = None
        username = None
        password = None
        terms = None
        is_added = None

        #Get Values From The Form
        if 'first_name' in request.POST : first_name = request.POST['first_name']
        else : messages.error(request,'Error In First Name')

        if 'last_name' in request.POST : last_name = request.POST['last_name']
        else : messages.error(request,'Error In Last Name')

        if 'address' in request.POST : address = request.POST['address']
        else : messages.error(request,'Error In Address')

        if 'address2' in request.POST : address2 = request.POST['address2']
        else : messages.error(request,'Error In Address2')

        if 'city' in request.POST : city = request.POST['city']
        else : messages.error(request,'Error In City')

        if 'state' in request.POST : state = request.POST['state']
        else : messages.error(request,'Error In State')

        if 'zip_number' in request.POST : zip_number = request.POST['zip_number']
        else : messages.error(request,'Error In Zip Number')

        if 'email' in request.POST : email = request.POST['email']
        else : messages.error(request,'Error In Email')

        if 'username' in request.POST : username = request.POST['username']
        else : messages.error(request,'Error In Username')

        if 'password' in request.POST : password = request.POST['password']
        else : messages.error(request,'Error In Password')

        if 'terms' in request.POST : terms = request.POST['terms']

        #Check the values
        if first_name and last_name and address and address2 and city and zip_number and state and email and username and password :
            if terms == 'on' :
                #Check if username is taken
                if User.objects.filter(username=username).exists():
                    messages.error(request,'Username Is Taken')
                else :
                    #Check if email is taken
                    if User.objects.filter(email=email).exists():
                        messages.error(request,'This Email Is Taken')
                    else :
                        patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                        if re.match(patt , email):
                            # add user
                            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                            user.save()
                            # add user profile
                            userprofile = UserProfile(user=user,address=address,address2=address2,city=city,state=state,zip_number=zip_number)
                            userprofile.save()
                            #clear fields
                            first_name = ''
                            last_name = ''
                            address = ''
                            address2 = ''
                            city = ''
                            state = ''
                            zip_number = ''
                            username = ''
                            password = ''
                            email = ''
                            terms = None
                            #Success Message
                            messages.success(request , 'Your Is Created Successfully')
                            is_added = True
                        else :
                            messages.error(request,'Invalid Email')



            else : 
                messages.error(request,'You Must Agree The Terms')

        else :
            messages.error(request,'Check Empty Fields')

        return render(request , 'signup.html',{
            'first_name': first_name , 
            'last_name': last_name , 
            'address': address , 
            'address2': address2 , 
            'city': city , 
            'zip_number': zip_number , 
            'state': state , 
            'email': email , 
            'username': username , 
            'password': password ,
            'is_added' : is_added
        })
    else:
        return render(request , 'signup.html')
    


def profile(request):
    if request.method == 'POST' and 'btn_save' in request.POST:
        messages.info(request,'test and btn_save')
        return redirect('profile')
    else:
        return render(request , 'profile.html')
    