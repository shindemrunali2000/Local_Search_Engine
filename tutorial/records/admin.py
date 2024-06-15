from django.contrib import admin
from .models import record_data,record_teacher,record_family,adverties_data,Contact_us
# Register your models here.

admin.site.register(record_data)
admin.site.register(record_teacher)

admin.site.register(record_family)

admin.site.register(adverties_data)

admin.site.register(Contact_us)