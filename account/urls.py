from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage,name='home'),
    path('news/', views.news,name='news'),
    path('studentform/', views.studentForm,name='studentForm'),
    path('contactus/', views.contactUs,name='contactUs'),
    path('loginpage/', views.loginPage,name='loginPage'),
    path('login/', views.auth_login,name='login'),
    path('register/', views.register,name='register'),
    path('adminpage/', views.adminPage, name='adminPage'),
    path('student/', views.studentPage, name='studentPage'),
    path('teacher/', views.teacherPage, name='teacherPage'),
]