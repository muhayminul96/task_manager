from django.contrib.auth import authenticate,login,logout
from django.shortcuts import HttpResponse ,render,redirect
from django.contrib.auth.models import User
from django.contrib import messages



def user_login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is None:
            messages.add_message(request, messages.ERROR, "Username  and password not match")
            return render(request, 'login.html')
        else:
            login(request,user)
            return redirect('/task/')

        

        print(password,email)

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        password = request.POST['password']
        re_password = request.POST['re-password']
        user = User.objects.filter(username=username)

        if(password != re_password):
            messages.add_message(request, messages.ERROR, "password and confirm password not match")
            return render(request, 'register.html')
        elif user.exists():
            messages.add_message(request, messages.ERROR, "username already exists")
            return render(request, 'register.html')
        user = User.objects.create(
            first_name = fullname,
            username = username,

        )
        user.set_password(password)
        user.save()
        print(username,fullname,password,re_password)

          
    return render(request, 'register.html')