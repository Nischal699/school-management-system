from django.contrib import admin
from django.urls import path
from mainSite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name='home'),
    path('introduction/', views.introduction,name='introduction'),
    path('preschool/', views.preSchool,name='preSchool'),
    path('primaryschool/', views.primarySchool,name='primarySchool'),
    path('secondaryschool/', views.secondarySchool,name='secondarySchool'),
    path('admission/', views.admission,name='admission'),
    path('news/', views.news,name='news'),
    path('studentform/', views.studentForm,name='studentForm'),
    path('paymentnotice/', views.paymentNotice,name='paymentNotice'),
    path('contactus/', views.contactUs,name='contactUs'),
    path('adminlogin/', views.adminLogin,name='adminLogin'),
    path('teacherlogin/', views.teacherLogin,name='teacherLogin'),
    path('studentlogin/', views.studentLogin,name='studentLogin'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
