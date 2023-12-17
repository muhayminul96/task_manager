from django.contrib.auth import authenticate
from django.shortcuts import HttpResponse ,render


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
    return render(request, 'register.html')