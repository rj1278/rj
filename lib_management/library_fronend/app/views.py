
from email import header
from importlib.resources import path
from turtle import RawTurtle
from wsgiref.util import request_uri
from django.http import HttpResponseRedirect
from django.shortcuts import render
import json,requests
from .models import GetUser
# Create your views here.
req_url='http://192.168.43.171:8082'

auth=GetUser()

def admin_signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']

        data={
            "username": username,
            "password": password,
            "password2": password2,
            "email": email,
            "first_name": first_name,
            "last_name":last_name
            }
        data_json=json.dumps(data)
        header={'Content-Type':'application/json'}
        url=f'{req_url}/library/signup/'
        res=requests.post(url,headers=header,data=data_json)
        print(res.text)
        data=json.loads(res.text)
        try:
            if data['status'] == 200:
                auth.set_email(email=email)
                return HttpResponseRedirect('/signin')
        except:
            pass
    return render(request,'signup.html')

def login_view(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        data={
            "emailId": email,
            "password": password
         }
        print(data)
        data_json=json.dumps(data)
        header={'Content-Type':'application/json'}
        url=f'{req_url}/library/admin/login/'
        res=requests.post(url,data_json,headers=header)
        data=json.loads(res.text)
        if data['status'] == 200:
            auth.set_email(email=email)
            return HttpResponseRedirect('/book_view')
    return render(request,'signin.html')

def book_view(request):
    books=get_data(request,f'{req_url}/library/book/get/')
    context={'books':books}
    if request.method=='POST':
        book_name=request.POST['book_name']
        author=request.POST['author']
        serial_no=request.POST['serial_no']
        category=request.POST['category']
        param={
            'email':auth.get_email()
        }
        data={
            "book_name":book_name,
            "author": author,
            "serial_no": serial_no,
            "category": category
            }
        data_json=json.dumps(data)
        header={'Content-Type':'application/json'}
        url=f'{req_url}/library/book/'
        res=requests.post(url,headers=header,data=data_json,params=param)
        data=json.loads(res.text)
        print(data)
        if data['status'] == 200:
            return HttpResponseRedirect('/book_view')
        
    return render(request,'book_view.html',context) 
def update_book(request):
    if request.method=='POST':
        id=request.POST['id']
        book_name=request.POST['book_name']
        author=request.POST['author']
        serial_no=request.POST['serial_no']
        category=request.POST['category']
        param={
            'email':auth.get_email()
        }
        data={
            "id":id,
            "book_name":book_name,
            "author": author,
            "serial_no": serial_no,
            "category": category
            }
        data_json=json.dumps(data)
        header={'Content-Type: application/json'}
        url=f'{req_url}/library/book/update_book/'
        res=requests.post(url,headers=header,data=data_json,params=param)
        data=json.loads(res.text)
        if data['status'] == 200:
            return HttpResponseRedirect('/book_view')

def del_book(request):
    if request.method=='POST':
        id=request.POST['id']
        param={
            'email':auth.get_email(),
            'id':id
        }
        res=requests.delete(f'{req_url}/library/book/delete_book',params=param)
        data=json.loads(res.text)
        if data['status'] == 200:
            return HttpResponseRedirect('/book_view')
        return HttpResponseRedirect('/book_view')
        
def student_view(request):
    books=get_data(request,f'{req_url}/library/book/get/')
    # print(books)
    context={'books':books}
    return render(request,'home.html',context)


def get_data(request,url):
    res=requests.get(url)
    data=json.loads(res.text)
    return data

