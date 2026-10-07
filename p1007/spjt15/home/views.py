from django.shortcuts import render

from django.shortcuts import render

#메인페이지
def index(request):
    return render(request,'index.html')

