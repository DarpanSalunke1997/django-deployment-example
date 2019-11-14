from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, UserProfileInfoForm

#Below imports for Login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def base_index(request):
    return render(request,'basic_app/index.html')

def base_other(request):
    context_dir = {'text':"Hello This Is Text",'num':100}
    return render(request,'basic_app/other.html',context_dir)

def base_relative(request):
    return render(request,'basic_app/relative_url_template.html')

def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered=True

        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'basic_app/registration.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})

@login_required
def special(request):
    return HttpResponse("<h1>You Login , Nice</h1>")

@login_required
def user_logout(request):
    logout(request)
    return render(request,'basic_app/index.html')

def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'basic_app/index.html')
            else:
                return HttpResponse("ACOUNT NOT ACTIVATE")
        else:
            print("SOME ONE TRING TO LOGIN")
            print(f"Username : {username} and Password : {password}")
            print("INVALID LOGIN DETAIL SUPPLIED!.")
            return render(request,'basic_app/login.html')
    else:
        return render(request,'basic_app/login.html')


