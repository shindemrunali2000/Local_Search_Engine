from django.db import models


# Create your models here.

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
    # product_Image=models.ImageField(upload_to='adverties/image',default=0)
    
    
    def __str__(self):
        return f"{self.name} {self.email}"