from django.contrib.auth import authenticate
from django.shortcuts import HttpResponse ,render
from django.contrib.auth.models import User


def home (request):
    name_list = ['amina','tumina','akash','batash']
    context = {
        "name": name_list
    }
    return render(request,'home/index.html',context)

def login(request):
    print(request)

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        print(user)

        

        print(password,email)

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        password = request.POST['password']
        re_password = request.POST['re-password']
        user = User.objects.create(
            first_name = fullname,
            username = username,

        )
        user.set_password(password)
        user.save()
        print(username,fullname,password,re_password)

          
    return render(request, 'register.html')