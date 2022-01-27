from attr import fields
from django.forms import models
from numpy import source
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Admin_User, Book
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Admin_User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Admin_User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
class SaveRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Admin_User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True)
    

    class Meta:
        model = Admin_User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    # def create(self, validated_data):
    #     user = Admin_User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         password=validated_data['password']
    #     )
    #     user.save()

    #     return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
class UpdateBookSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    bookName=serializers.CharField(source='book_name')
    author=serializers.CharField()
    serialNo=serializers.CharField(source='serial_no')
    category=serializers.CharField()
    class Meta:
        model=Book
        fields=('id','bookName','author','category','serialNo')
    

class LoginSerializer(serializers.Serializer):
    emailId=serializers.EmailField()
    password=serializers.CharField()

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
#  7358312383
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

