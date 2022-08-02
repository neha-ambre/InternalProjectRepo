"""iternal_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include,re_path
from iternal_project import views
from members import views as memViews
from api import views as apiViews

admin.site.site_header = "Name of the Admin"
admin.site.index_title = "Welcome "
admin.site.site_title = "Weilcome"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="iternal_project"),
    path('formSubmitted/index/',views.index,name="iternal_project"),
    path('index/',views.index,name="iternal_project"),
    path('temp',apiViews.temp,name="temp"),
    path('signUp',memViews.signUp,name="signUp"),
    path('saveUser/',memViews.saveUser,name='saveUser'),
    path('login/saveForm/',apiViews.saveForm,name='login_saveForm'),
    path('members/login/saveForm/',apiViews.saveForm,name='loginSaveForm'),
    # path('login/fillForm/',memViews.fillForm,name='login_fillForm'),
    path('fillForm/',memViews.fillForm,name='fillForm'),
    path('fillForm/saveForm/',apiViews.saveForm,name='saveForm'),
    path('formSubmitted/',apiViews.formSubmitted,name='formSubmitted'),
    
    path('saveForm/',apiViews.saveForm,name='saveForm'),
    # path('saveForm/formSubmitted/',apiViews.formSubmitted,name='saveFormSubmitted'),
    # path('/saveForm/formSubmitted/',apiViews.formSubmitted,name='saveFormSubmitted'),
    # # path('/saveForm/',apiViews.formSubmitted,name='saveFormSubmitted'),
    
    # path('/formSubmitted/',apiViews.formSubmitted,name='FormSubmitted'),
    path('getUser/',memViews.getUser,name='getUser'),   
    path('login/',memViews.login_user,name='login'),
    path('logout/',memViews.logout_user,name='login'), 
    path('members/',include('members.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('excel/',apiViews.ExportImportExcel.as_view())
]
