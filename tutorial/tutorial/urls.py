from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from tutorial import settings
# from records import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("records.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

