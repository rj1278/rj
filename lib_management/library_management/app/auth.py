
from rest_framework.response import Response
from rest_framework.views import APIView    
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authentication import SessionAuthentication

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Get the username and password
        username = request.data.get('username', None)
        password = request.data.get('password', None)