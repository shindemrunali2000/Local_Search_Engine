from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from tutorial import settings
from .views import first_page,input_data,input_data1,contact_us, register_business, success,vdarpan,input_data2,adverties,Marathi
from records import views
from django.contrib.auth.views import LogoutView 
from . import views
urlpatterns = [
    path('', views.project, name='project'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('laptops/', views.laptop_posts, name='laptop_posts'),
    path('contact-us/', contact_us, name='contact_us'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path("records/",input_data,name="records.html"),
    path("teachers/",input_data1,name="records1.html"),
    path('vdarpan/',vdarpan,name="vdarpan.html"),
    path('index/',first_page,name="index.html"),
    path("family/",input_data2,name="family.html"),
    path("adverties/",adverties,name="add.html"),
    path("Marathi/",Marathi,name="Marathi.html"),
    path('register/', register_business, name='register_business'),
    path('success/', success, name='business_success'),  
    path('restaurants/', views.restaurants_blog, name='restaurants_blog'),
    path('electronics/', views.electronics_blog, name='electronics_blog'),
    path('cloths/', views.cloths_blog, name='cloths_blog'),
    path('college/', views.college_blog, name='college_blog'),
    path('carrent/', views.car_rent_blog, name='car_rent_blog'),
    path('fitness/', views.fitness_blog, name='fitness_blog'),
    path('home_service/', views.home_service_blog, name='home_service_blog'),
    path('travels/', views.travels_blog, name='travels_blog'),
    path('logistics/', views.logistics_blog, name='logistics_blog'),
    path('event_organizer/', views.event_organizer_blog, name='event_organizer_blog'),
    path('doctor/', views.doctor_blog, name='doctor_blog'),
    path('entertainment/', views.entertainment_blog, name='entertainment_blog'),
    path('photography/', views.photography_blog, name='photography_blog'),
    path('clinics/', views.clinics_blog, name='clinics_blog'),
    path('jewelry/', views.jewelry_blog, name='jewelry_blog'),
    path('school/', views.school_blog, name='school_blog'),
    path('search-results/', views.search_results, name='search_results'),
    path('business/<int:business_id>/', views.business_detail, name='business_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
