from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms



choice=(('java','java'),
        ('python','python'),
        ('javascript','javascript'),
        )

class record_data(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    course=models.CharField(max_length=20)
    collegename=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class record_teacher(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    subject=models.CharField(max_length=10,choices=choice,default="java")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class record_family(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class adverties_data(models.Model):
    product_Name=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    price=models.IntegerField(default=0)
    location_City=models.CharField(max_length=20)
    contact_Number=models.IntegerField(default=0)
    product_Image=models.ImageField(upload_to='adverties/image',default=0)
    
    
    def __str__(self):
        return f"{self.product_Name} {self.category}"
    


class Contact_us(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.IntegerField(default=0)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=20)
    
    
    
    def __str__(self):
        return f"{self.name} {self.email}"
    



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')
    email = forms.EmailField(max_length=254, required=True, help_text='Valid email address required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.user.username


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"



class Business(models.Model):
    name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)
    location_city = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    owner_name = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='business_images/')

    def __str__(self):
        return f"{self.name} - {self.business_type}"