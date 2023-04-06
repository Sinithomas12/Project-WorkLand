"""city360 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('services/', views.services),
    path('about/', views.about),
    
    path('login/', views.login),
    path('userregistration/', views.userregistration),
    path('workerregistration/', views.workerregistration),
    
    path('admin_home/', views.admin_home),
    path('addcategory/', views.addcategory),
    path('viewuser/', views.viewuser),
    path('approveuser/', views.approveuser),
    path('rejecteduser/', views.rejecteduser),
    path('deleteuser/', views.deleteuser),
    path('viewworker/', views.viewworker),
    path('approveworker/', views.approveworker),
    path('rejectedworker/', views.rejectedworker),
    path('deleteworker/', views.deleteworker),
    path('userfeedback/', views.userfeedback),
    path('viewcategory/', views.viewcategory),
    path('deletecategory/', views.deletecategory),
    path('workerfeedback/', views.workerfeedback),
    
    path('user_home/', views.user_home),
    path('userviewcategory/', views.userviewcategory),
    path('bookingcategory/', views.bookingcategory),
    path('bookworker/', views.bookworker),
    path('userviewbooking/', views.userviewbooking),
    path('cancelbooking/', views.cancelbooking),
    path('useraddfeedback/', views.useraddfeedback),
    path('userviewfeedback/', views.userviewfeedback),
    path('addfeedback/', views.addfeedback),
    path('userprofile/', views.userprofile),
    path('updateuser/', views.updateuser),
    path('payment/', views.payment),
    path('userviewpayment/', views.userviewpayment),
    
    path('worker_home/', views.worker_home),
    path('workerviewbooking/', views.workerviewbooking),
    path('approvebooking/', views.approvebooking),
    path('rejectbooking/', views.rejectbooking),
    path('deletebooking/', views.deletebooking),
    path('workerviewfeedback/', views.workerviewfeedback),
    path('workeraddfeedback/', views.workeraddfeedback),
    path('workerprofile/', views.workerprofile),
    path('updateworker/', views.updateworker),
    path('workerviewpayment/', views.workerviewpayment),
    path('deletepayment/', views.deletepayment),
    
    
    
    
]
