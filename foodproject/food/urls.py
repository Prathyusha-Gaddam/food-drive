from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('accounts/profile/',views.index,name='index'),
    path('accounts/profile/index',views.index,name='index'),
    path('accounts/profile/#',views.getdetails,name='getdetails'),
    path('getdetails',views.getdetails,name='getdetails'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='food/login.html'),name='login'),
    path('login1',auth_views.LoginView.as_view(template_name='food/login1.html'),name='login1'),
    path('logout',auth_views.LogoutView.as_view(template_name='food/logout.html'),name='logout'),
]