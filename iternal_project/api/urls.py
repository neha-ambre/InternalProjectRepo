from django.urls import path,include
from api import views

urlpatterns = [   
    path('about',views.about,name="api"), #there is function named about in views.py file which will be executed if user add /about in the url
    path('contact',views.contactus,name="api"),
    path('temp',views.temp,name="temp"),
    # path('login',views.login,name="login"),
    path('signUp',views.signUp,name="signUp"),
    # path('form',views.exampleForm,name='exampleForm'),
    path('saveForm/',views.saveForm,name='saveForm'),
    path('login/saveForm/',views.saveForm,name='saveForm'),
    path('saveUser/',views.saveUser,name='saveUser'),
    path('getUser/',views.getUser,name='getUser'),
]