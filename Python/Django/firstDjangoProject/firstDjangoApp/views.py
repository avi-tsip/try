from django.shortcuts import render
from django.http import HttpResponse

# HelloWorld View
def index(request):
    return HttpResponse('Hello World!')
