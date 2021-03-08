from .views import TodoList,DetailTodo,RegisterUser
from django.urls import path
from  rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path("register/",RegisterUser.as_view(), name="register"),



    path('todos/',TodoList.as_view(),name="todo-list"), 
    path('todos/<int:pk>', DetailTodo.as_view(),name="detail-list"),
    
    
]
