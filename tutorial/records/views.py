
from django.shortcuts import get_object_or_404, render,redirect
from .models import adverties_data, record_data, ContactUs, Business,record_teacher,record_family,Contact_us,Profile
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('project')
    else:
        form = SignupForm()
    return render(request, "..\Templete\HTML\\signup.html", {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('project')
    else:
        form = LoginForm()
    return render(request, "..\Templete\HTML\\login.html", {'form': form})

@login_required
def project(request):
    return render(request, "..\Templete\HTML\\project.html")


def first_page(request):
    records=record_data.objects.all()
    print(records)
    context={
        "records":records,
    }
    return render(request, '..\Templete\index.html',context)

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
    


    
       myquery=Contact_us(name=name,email=email,phone=phone,subject=subject,message=message)
       myquery.save()
    return render(request,"..\Templete\HTML\\Contact_us.html")


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactUs.objects.create(
            name=name,
            email=email,
            contact_number=contact_number,
            subject=subject,
            message=message
        )
        return HttpResponse("Thank you for contacting us!")
    
    return render(request, "..\Templete\HTML\\contact_us.html")





# def laptop_posts(request):
#     laptops = adverties_data.objects.filter(product_Name__iexact='Laptop') 
#     return render(request, '..\Templete\HTML\\laptop_posts.html', {'laptops': laptops})




def success(request):
    return render(request, '..\Templete\HTML\\success.html')


def register_business(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        business_type = request.POST.get('business_type')
        location_city = request.POST.get('location_city')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        owner_name = request.POST.get('owner_name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        
        Business.objects.create(name=name,business_type=business_type,location_city=location_city,contact_number=contact_number,address=address,owner_name=owner_name,description=description,image=image
        )
        return redirect('business_success') 

    return render(request, '..\Templete\HTML\\Free_Listing.html')


def restaurants_blog(request):
    restaurants = Business.objects.filter(business_type='Restaurants') 
    return render(request, '..\Templete\HTML\\Restaurants_blog.html', {'restaurants': restaurants})



def electronics_blog(request):
    electronics = Business.objects.filter(business_type='Electronics')
    return render(request, '..\Templete\HTML\\electronics_blog.html', {'electronics': electronics})


def cloths_blog(request):
    cloths = Business.objects.filter(business_type='Cloths')
    return render(request, '..\Templete\HTML\\cloths_blog.html', {'cloths': cloths})


def college_blog(request):
    colleges = Business.objects.filter(business_type='College')
    return render(request, '..\Templete\HTML\\college_blog.html', {'colleges': colleges})


def car_rent_blog(request):
    car_rentals = Business.objects.filter(business_type='Automobile')
    return render(request, '..\Templete\HTML\\car_rent_blog.html', {'car_rentals': car_rentals})

def fitness_blog(request):
    fitness_centers = Business.objects.filter(business_type='Fitness')
    return render(request, '..\Templete\HTML\\fitness_blog.html', {'fitness_centers': fitness_centers})

# Continue for other categories...
def home_service_blog(request):
    home_services = Business.objects.filter(business_type='Home Service')
    return render(request, '..\Templete\HTML\\home_service_blog.html', {'home_services': home_services})


def travels_blog(request):
    Travels = Business.objects.filter(business_type='Travels')
    return render(request, '..\Templete\HTML\\travels_blog.html', {'Travels': Travels})

def logistics_blog(request):
    Logistics = Business.objects.filter(business_type='Logistics')
    return render(request, '..\Templete\HTML\\logistics_blog.html', {'Logistics': Logistics})

def event_organizer_blog(request):
    event_organizers = Business.objects.filter(business_type='Event Organizer')
    return render(request, '..\Templete\HTML\\event_organizer_blog.html', {'event_organizers': event_organizers})

def doctor_blog(request):
    Doctors = Business.objects.filter(business_type='Doctors')
    return render(request, '..\Templete\HTML\\doctor_blog.html', {'Doctors': Doctors})

def entertainment_blog(request):
    Entertainments = Business.objects.filter(business_type='Entertainment')
    return render(request, '..\Templete\HTML\\entertainment_blog.html', {'Entertainments': Entertainments})

def photography_blog(request):
    Photographys = Business.objects.filter(business_type='Photography')
    return render(request, '..\Templete\HTML\\photography_blog.html', {'Photographys': Photographys})

def clinics_blog(request):
    clinics = Business.objects.filter(business_type='clinics')
    return render(request, '..\Templete\HTML\\clinics_blog.html', {'clinics ': clinics })

def jewelry_blog(request):
    jewellres = Business.objects.filter(business_type='jewellres')
    return render(request, '..\Templete\HTML\\jewelry_blog.html', {'jewellres': jewellres})

def school_blog(request):
    schools = Business.objects.filter(business_type='schools')
    return render(request, '..\Templete\HTML\\school_blog.html', {'schools': schools})




def search_results(request):
    location_city = request.GET.get('location_city')
    business_type = request.GET.get('business_type')

    # Filter the businesses based on city and type
    results = Business.objects.filter(location_city=location_city, business_type=business_type)

    context = {
        'results': results,
        'location_city': location_city,
        'business_type': business_type,
    }
    
    return render(request, '..\Templete\HTML\\search_results.html', context)

   
def business_detail(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    return render(request, '..\Templete\HTML\\business_detail.html', {'business': business})