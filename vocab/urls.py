from django.contrib import admin
from django.urls import path,include
from vocab import views




urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('day/<int:myid>/test',views.test,name="test"),
    path('signup/', views.handleSignup, name='signup'),
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handleLogout, name='logout'),

    

]