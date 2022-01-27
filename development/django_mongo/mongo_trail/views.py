from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def page(request):
    return HttpResponse('fff')