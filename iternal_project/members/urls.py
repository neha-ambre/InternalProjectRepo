from django.urls import path
from members import views

urlpatterns = [ 
    path('login/',views.login_user,name='loginuser'),
    path('signUp',views.signUp,name="signUp"),
    path('saveUser/',views.saveUser,name='saveUser'),
    path('getUser/',views.getUser,name='getUser'),
    # path('fillForm/',views.fillForm,name='fillForm'),
]