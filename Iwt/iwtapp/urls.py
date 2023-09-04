"""
URL configuration for Iwt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('companies',views.companies,name="companies"),
    path('login',views.login,name="login"),
    path('support',views.support,name="support"),
    path('hcl',views.hcl,name="hcl"),
    path('deloitte',views.deloitte,name="deloitte"),
    path('google',views.google,name="google"),
    path('ibm',views.ibm,name="ibm"),
    path('intel',views.intel,name="intel"),
    path('jpmc',views.jpmc,name="jpmc"),
    path('template',views.template,name="template"),
    path('meta',views.meta,name="meta"),
    path('microsoft',views.microsoft,name="microsoft"),
    path('oracle',views.oracle,name="oracle"),
    path('qualcomm',views.qualcomm,name="qualcomm"),
    path('salesforce',views.salesforce,name="salesforce"),
    path('tcs',views.tcs,name="tcs"),
    path('accenture',views.accenture,name="accenture"),
    path('amazon',views.amazon,name="amazon"),
    path('signup',views.signup,name="signup"),
    path('signup',views.signup,name="signup"),
    path('login_user',views.login_user,name="login"),
    path('logout_user',views.logout_user,name="logout"),
    path('details',views.details,name='details'),
    path('submit_form_view', views.submit_form_view, name='submit_form_view'),
]
