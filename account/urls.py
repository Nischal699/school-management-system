from django.urls import path
from mainSite import views

urlpatterns = [
    path('', views.homePage,name='home'),
    path('news/', views.news,name='news'),
    path('studentform/', views.studentForm,name='studentForm'),
    path('contactus/', views.contactUs,name='contactUs'),
    path('adminlogin/', views.adminLogin,name='adminLogin'),
    path('teacherlogin/', views.teacherLogin,name='teacherLogin'),
    path('studentlogin/', views.studentLogin,name='studentLogin'),
    
    
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    
]