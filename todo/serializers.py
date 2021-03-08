#django
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.models import User
#django_rest
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
#app
from .models import Todo
from django.contrib.auth.models import User
class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = User
        fields = ("email","username")

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        

        model = Todo
        fields = '__all__'
        read_only_fields = ['username']
       
class UserSignUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    def validate(self, data):
        
        passwd = data['password']
        print(passwd)
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user


    
        


