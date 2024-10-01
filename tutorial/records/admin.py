from django.contrib import admin
from .models import Business, record_data,record_teacher,ContactUs,Profile,record_family,adverties_data,Contact_us,User
# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin


admin.site.register(record_data)
admin.site.register(record_teacher)

admin.site.register(record_family)

admin.site.register(adverties_data)

admin.site.register(Contact_us)

admin.site.register(Profile)
admin.site.register(ContactUs)
admin.site.register(Business)


