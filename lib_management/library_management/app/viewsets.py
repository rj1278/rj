from importlib_metadata import re
from rest_framework.schemas.openapi import AutoSchema
from django.http import response
from torch import serialization
from .models import Admin_User,Book
from rest_framework import viewsets,generics
from .serializers import BookSerializer, RegisterSerializer,LoginSerializer,UserRegisterSerializer,\
    UpdateBookSerializer,SaveRegisterSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
# from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.authentication import BaseAuthentication
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from .schema import CustomSchema,IdCustomSchema


# from  import serializers


class RegisterViewset(generics.ListCreateAPIView):
    schema=AutoSchema(tags=['Admin Controller'])
    serializer_class=RegisterSerializer
    queryset=Admin_User.objects.all()

class RegisterViewset(viewsets.GenericViewSet):
    schema=AutoSchema(tags=['Admin Controller'])
    serializer_class=RegisterSerializer
    queryset=Admin_User.objects.all()
    def create(self,request):
        if request.data['password'] != request.data['password2']:
            raise Response({"status":status.HTTP_400_BAD_REQUEST,'message': "Password fields didn't match."})
        data=request.data
        print(data)
        del data['password2']
        serializer=SaveRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('saved')
            return Response({'status':status.HTTP_200_OK})
        return Response({'status':status.HTTP_400_BAD_REQUEST,'message':serializer.errors})

class LoginViewset(viewsets.GenericViewSet):
    serializer_class=LoginSerializer
    schema=AutoSchema(tags=['Login Controller'])
    queryset=Admin_User.objects.all()
    @action(methods=['post'],detail=False)
    def login(self,request):
        try:
            user=self.queryset.get(email=request.data['emailId'],password=request.data['password'])
        except ObjectDoesNotExist:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'Invalid Credentialis'})
        return Response({'status':status.HTTP_200_OK,'message':'You logged in successfully'})
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

def validate(email):
    try:
        Admin_User.objects.get(email=email)
        return True
    except ObjectDoesNotExist:
        return False

class BookViewset(viewsets.GenericViewSet):
    schema=CustomSchema(tags=['Book Controller'])
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def create(self,request):
        data=validate(request.query_params.get("email"))
        if data:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({'status':status.HTTP_200_OK})
        return Response({'status':status.HTTP_401_UNAUTHORIZED})
    @action(methods=['get'],detail=False,schema=AutoSchema(tags=['Book Controller']))
    def get(self,request):
        serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(serializer.data)
   

class UpdateViewset(viewsets.GenericViewSet):
    schema=CustomSchema(tags=['Book Controller'])
    queryset = Book.objects.all()
    serializer_class=UpdateBookSerializer
    @action(methods=['put'],detail=False,schema=CustomSchema(tags=['Book Controller']))
    def update_book(self,request):
        data=validate(request.query_params.get("email"))
        if data:
            instance=self.queryset.get(pk=request.data['id'])
            serializer=self.serializer_class(instance=instance,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response({'status':status.HTTP_200_OK})
        return Response({'status':status.HTTP_401_UNAUTHORIZED})
    @action(methods=['delete'],detail=False,schema=IdCustomSchema(tags=['Book Controller']))
    def delete_book(self,request):
        data=validate(request.query_params.get("email"))
        if data:
            try:
                instance = self.queryset.filter(id=request.query_params.get("id"))
                instance.delete()
                return Response({'status':status.HTTP_200_OK})
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'status':status.HTTP_401_UNAUTHORIZED})






