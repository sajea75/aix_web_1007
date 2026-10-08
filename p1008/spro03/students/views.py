from django.shortcuts import render

# 학생성적입력
def swrite(request):
    return render(request,'swrite.html')

# 학생성적리스트
def slist(request):
    return render(request,'slist.html')
