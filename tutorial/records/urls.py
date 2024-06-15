from django.contrib import admin
from django.urls import path,include
from .views import first_page,login,LogoutPage,input_data,input_data1,vdarpan,login1,project,signup,input_data2,adverties,contactus,Marathi
from records import views

urlpatterns = [
    path("",project,name="project.html"),
    # path("signup/",signup,name="signup.html"),
    path("login/",login,name="login.html"),
    path("login/",LogoutPage,name='login.html'),
    path("login1/",login1,name='login1.html'),
    path("records/",input_data,name="records.html"),
    path("teachers/",input_data1,name="records1.html"),
    path('vdarpan/',vdarpan,name="vdarpan.html"),
    path('index/',first_page,name="index.html"),
    path("signup/",signup,name="signup_data.html"),
    path("family/",input_data2,name="family.html"),
    path("adverties/",adverties,name="add.html"),
    path("contactus/",contactus,name="Contact_us.html"),
    path("Marathi/",Marathi,name="Marathi.html"),



]


