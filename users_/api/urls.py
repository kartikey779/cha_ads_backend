from users_ import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', views.Users, name='users'),
    path('loginA/', obtain_auth_token, name='loginA'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]