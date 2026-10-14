from django.shortcuts import render,redirect

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')
