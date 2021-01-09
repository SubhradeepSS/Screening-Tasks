from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('MAIN:Login')
    return render(request, "MAIN/index.html")

def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('MAIN:index')
        
        else:
            return redirect('MAIN:Login')
        
    return render(request, "MAIN/login.html")

def Logout(request):
    logout(request)
    return redirect("MAIN:Login")