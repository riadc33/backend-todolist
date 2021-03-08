from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response  import Response
from django.http import Http404
from .models import Todo
from .serializers import TodoSerializer,UserModelSerializer,UserSignUpSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.decorators import action

class TodoList(APIView):
    def get(self,request):  
        permission_classes = [IsAuthenticated]
        todos = Todo.objects.filter(username=request.user)
        todo_json = TodoSerializer(todos,many=True)
        return Response(todo_json.data)

    def post(self,request):
        permission_classes = [IsAuthenticated]
        todo_json = TodoSerializer(data=request.data)
        print(todo_json)
        if todo_json.is_valid():
            todo_json.save(username=request.user)
            return Response(todo_json.data,status= 201)
        return Response(todo_json.errors,status=400)
        print(request.user.pk)
        return HttpResponse('request')
        pass

class DetailTodo(APIView):
    
    def get_object(self,pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def put(self, request,pk):
        
        todo = self.get_object(pk)
        todo_json = TodoSerializer(todo, data=request.data)
        if todo_json.is_valid():
            todo_json.save()
            return Response(todo_json.data)
        return Response(todo_json.errors, status=400 ) 

    def get(self,request,pk):   
        todo=self.get_object(pk)
        todo_json=TodoSerializer(todo)
        return Response(todo_json.data)

    def delete(self, request,pk):
        todo=self.get_object(pk)
        print(todo)
        todo.delete()
        return Response(status=204)
class RegisterUser(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)




        
        

        
   
    