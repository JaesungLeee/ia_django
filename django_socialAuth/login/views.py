# 어떤 상황의 데이터를 어떻게 처리할지 정의하는 file
from django.shortcuts import render

# Create your views here.
def home(request):  
    return render(request, 'home.html')  # request가 들어왔을때 home.html을 보여줌