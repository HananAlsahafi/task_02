from django.shortcuts import render
from django.http import HttpResponse
def home (request):
    text={
        "msg":"Hello, django",
        "title":"My First Django App"
    }
    return render(request,'hello.html',text)
