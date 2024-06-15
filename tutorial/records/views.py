from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import adverties_data, record_data, record_teacher,record_family,Contact_us
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout 
# Create your views here.

def first_page(request):
    records=record_data.objects.all()
    print(records)
    context={
        "records":records,
    }
    return render(request, '..\Templete\index.html',context)

# def signup(request):
#     if request.method=="POST":
#         email=request.POST['username']
#         print(email)
#         password=request.POST['password']
#         print(password)
#         confirm_password=request.POST['confirm_password']
#         print(email)
#         if password!=confirm_password:
#             return render(request,"..\Templete\HTML\signup.html")
#         try:
#             if User.objects.get(username=email):
#                 return render(request,"..\Templete\HTML\signup.html")
#         except Exception as identifier:
#             pass
#         user=User.objects.create_user(email,email,password)
#         user.is_active=True
#         user.save()
#     return render(request, '..\Templete\HTML\signup.html')




def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

    
        data =User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        data.save()
        data.is_active=True
    return render(request,"..\Templete\HTML\\signup_data.html")





def login(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['pass']
        myuser=authenticate(username=username,password=password)
        
        if myuser is not None:
            auth_login(request,myuser)
            print("login successful")
            return render(request,"..\Templete\HTML\index.html")
        else:
            print("unsuccesful login")
            return render(request,"..\Templete\HTML\login.html")
        
    return render(request,'..\Templete\HTML\login.html')

def login1(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['pass']
        myuser=authenticate(username=username,password=password)
        
        if myuser is not None:
            auth_login(request,myuser)
            print("login successful")
            return render(request,"..\Templete\index.html")
        else:
            print("unsuccesful login")
            return render(request,"..\Templete\login1.html")
        
    return render(request,'..\Templete\login1.html')

def LogoutPage(request):
    logout(request)

    return redirect('..\Templete\HTML\login.html')

def input_data(request):
    if request.method=='POST':
       first_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       age=request.POST.get('age')
       course=request.POST.get('course')
       collegename=request.POST.get('collegename')
       myquery=record_data(first_name=first_name,last_name=last_name,age=age,course=course,collegename=collegename)
       myquery.save()
    return render(request,"..\Templete\HTML\\records.html")


def input_data1(request):
    if request.method=='POST':
       first_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       subject=request.POST.get('subject')
       course=request.POST.get('course')
       collegename=request.POST.get('collegename')
       myquery=record_teacher(first_name=first_name,last_name=last_name,subject=subject)
       myquery.save()
    return render(request,"..\Templete\HTML\\records1.html")

 

def vdarpan(request):
    return render(request,"..\Templete\HTML\\vdarpan.html")

def project(request):
    return render(request,"..\Templete\HTML\project.html")


def Marathi(request):
    return render(request,"..\Templete\HTML\Marathi.html")


def input_data2(request):
    if request.method=='POST':
       first_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       age=request.POST.get('age')
    
       myquery=record_family(first_name=first_name,last_name=last_name,age=age)
       myquery.save()
    return render(request,"..\Templete\HTML\\family.html")



def adverties(request):
    if request.method=='POST':
       product_Name=request.POST.get('product_Name')
       category=request.POST.get('category')
       price=request.POST.get('price')
       location_City=request.POST.get('location_City')
       contact_Number=request.POST.get('contact_Number')
       product_Image=request.POST.get('product_Image')


    
       myquery=adverties_data(product_Name=product_Name,category=category,price=price,location_City=location_City,contact_Number=contact_Number,product_Image=product_Image)
       myquery.save()
    return render(request,"..\Templete\HTML\\add.html")



def contactus(request):
    if request.method=='POST':
       name=request.POST.get('name')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       subject=request.POST.get('subject')
       message=request.POST.get('message')
    #    product_Image=request.POST.get('product_Image')


    
       myquery=Contact_us(name=name,email=email,phone=phone,subject=subject,message=message)
       myquery.save()
    return render(request,"..\Templete\HTML\\Contact_us.html")