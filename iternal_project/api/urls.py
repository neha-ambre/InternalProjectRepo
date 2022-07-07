from django.urls import path
from api import views


urlpatterns = [
    path('',views.index,name="api"),  
    path('about',views.about,name="api"), #there is function named about in views.py file which will be executed if user add /about in the url
    path('contact',views.contactus,name="api"),
    path('temp',views.temp,name="temp"),
    # path('form',views.exampleForm,name='exampleForm'),
    path('saveForm/',views.saveForm,name='saveForm')
]