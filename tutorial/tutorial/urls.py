from django.contrib import admin
from django.urls import include, path
# from records import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("records.urls"))
]

