from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

#----------------HOME-PAGE--------------------
def homePage(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"index.html",data)

#----------------ABOUT-US----------------------
#Introduction
def introduction(request):
    return render(request,"introduction.html")


#----------------PROGRAMS----------------------

#Pre-school
def preSchool(request):
    return render(request,"pre-school.html")

#Primary-school
def primarySchool(request):
    return render(request,"primary-school.html")

#Secondary-school
def secondarySchool(request):
    return render(request,"secondary-school.html")


#-----------------ADMISSION-----------------------
def admission(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"admission.html",data)

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

#-------------------PAYEMENT NOTICE-----------------------
def paymentNotice(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"paymentNotice.html",data)

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
