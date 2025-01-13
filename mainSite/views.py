from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

#----------------HOME-PAGE--------------------
def homePage(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"index.html",data)

#-----------------NEWS/EVENTS----------------------
def news(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"news.html",data)

#------------------STUDENT FORM-------------------------
def studentForm(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"studentform.html",data)

#--------------------CONTACT US----------------------------
def contactUs(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"contactUs.html",data)


#----------------------LOGIN------------------------------
#ADMIN LOGIN
def adminLogin(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"adminLogin.html",data)

#TEACHER LOGIN
def teacherLogin(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"teacherLogin.html",data)

#STUDENT/PARENT LOGIN
def studentLogin(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"studentLogin.html",data)


#LOGIN
def login(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"login.html",data)

def register(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"register.html",data)
