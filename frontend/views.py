from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from . form import *
from django.http import HttpResponseBadRequest

from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
import threading
# Create your views here.

def Home(request):
    categories=Category.objects.all()
    context={
        'categories': categories,
    }
    return render(request, 'index.html', context)

def Shop(request):
    products=Product.objects.filter(show_product='YES')
    context={
        'products': products
    }
    return render(request, 'shop.html', context)

def ProductList(request, category_id=None):
    products = Product.objects.filter(show_product='YES')
    if category_id:
        category = Category.objects.get(pk=category_id)
        products = products.filter(category=category)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'category':category
    }
    return render(request, 'product_list.html', context)

def ProductDetails(request, pk):
    try:
        product = Product.objects.get(id=pk)
        brochure = Brochure.objects.get(product=product)
    except ObjectDoesNotExist:
        product = Product.objects.get(id=pk)
        brochure = None  # Set brochure to None or any default value you prefer

    similar_products = Product.objects.filter(category=product.category).exclude(id=pk)[:3]

    context = {
        'product': product,
        'similar_products': similar_products,
        'brochure': brochure
    }

    return render(request, 'product-details.html', context)

def About(request):
    return render(request, 'about.html')

def AllServices(request):
    servicescategory=ServiceCategory.objects.all()

    context={
        'servicescategory':servicescategory
    }
    return render(request, 'services.html', context)

def SingleServices(request, pk):
    # Retrieve the ServiceCategory object with the given primary key
    category = get_object_or_404(ServiceCategory, pk=pk)
    services = Services.objects.filter(category=category)



    context = {
        'services': services,
        'category': category,
    }
    return render(request, 'single_services.html', context)

def SingleServiceDetails(request,pk):
    
    service=Services.objects.get(pk=pk)

    context = {
        'service': service,
        
        }

    return render(request, 'single_service_details.html', context)

def Package(request):
    packages=Packages.objects.all()

    context={
        'packages': packages
    }
    return render(request, 'packages.html',context)

def PackageDeatils(request, pk):
    package=Packages.objects.get(pk=pk)

    context={
        'package': package
    }
    return render(request, 'package_deatils.html',context)

def Design(request):
    return render(request, 'design.html')

def Installation(request):
    return render(request, 'installation.html')

def Maintenance(request):
    return render(request, 'maintenance.html')

def BlogView(request):
    all_blog=Blog.objects.all()
    context={
        'all_blog':all_blog,
    }
    return render(request, 'blog.html', context)

def BlogDetailsView(request,pk):
    blog=Blog.objects.get(id=pk)
    context={
        'blog':blog,
    }
    return render(request, 'blog_details.html', context)

def ContactUs(request):

    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.save()
            email_thread = threading.Thread(target=contact_mail, args=(contact_instance, contact_instance.email))
            email_thread.start()
            return redirect ("/thanks/")

    else:
         form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)

def contact_mail(contact_instance, email,):
    subject = "Thanks we've got your message"
    from_email = "info@steuk.co.uk"
    to = [email, 'info@steuk.co.uk']  # Use the email parameter instead of string 'email'
    html_message= render_to_string('email/contact.html', {'contact_instance': contact_instance})
    plain_message = strip_tags(html_message)

    email_message = EmailMultiAlternatives(subject, plain_message, from_email, to=to)
    email_message.attach_alternative(html_message, "text/html")
    email_message.send()

def Thanks(request):

    return render(request, 'thanks.html')

def AdminView(request):

    category=Category.objects.all().count()
    product=Product.objects.all().count()
    allproduct=Product.objects.all()
    allcategory=Category.objects.all()
   

    context={
        'category': category,
        'product': product,
        'allproduct':allproduct,
        'allcategory':allcategory,

    }

    return render(request, 'backend/backend.html',context)

def formItems(request):

   
    all_blog=Blog.objects.all()

    context={
     
        'all_blog':all_blog,
    }

    return render(request, 'questionary.html' , context)

class BoilerForm(forms.Form):
    property_type = forms.CharField()
    job_type = forms.CharField()
    boiler_type = forms.CharField()
    power_usage = forms.CharField()
    name = forms.CharField()
    full_address = forms.CharField()
    post_code = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

def BoilerFormView(request):
    if request.method == 'POST':
        form = BoilerForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            boiler_data = Q_BoilerData(
                property_type=cleaned_data['property_type'],
                job_type=cleaned_data['job_type'],
                boiler_type=cleaned_data['boiler_type'],
                power_usage=cleaned_data['power_usage'],
                name=cleaned_data['name'],
                full_address=cleaned_data['full_address'],
                post_code=cleaned_data['post_code'],
                phone=cleaned_data['phone'],
                email=cleaned_data['email']
            )
            boiler_data.save()
            email_thread = threading.Thread(target=booking_email, args=(boiler_data, boiler_data.email,'boiler'))
            email_thread.start()
            return redirect('/')
    else:
        form = BoilerForm()
    return render(request, 'forms/Biolerform.html', {'form': form})
    
class EVChargerForm(forms.Form):
    installation_type = forms.CharField()
    ownership_type = forms.CharField()
    parking_type = forms.CharField()
    car_type = forms.CharField()
    charger_type = forms.CharField()
    name = forms.CharField()
    full_address = forms.CharField()
    post_code = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

def EVChargerFormView(request):
    if request.method == 'POST':
        form = EVChargerForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            ev_data = Q_EVData(
                installation_type=cleaned_data['installation_type'],
                ownership_type=cleaned_data['ownership_type'],
                parking_type=cleaned_data['parking_type'],
                car_type=cleaned_data['car_type'],
                charger_type=cleaned_data['charger_type'],
                name=cleaned_data['name'],
                full_address=cleaned_data['full_address'],
                post_code=cleaned_data['post_code'],
                phone=cleaned_data['phone'],
                email=cleaned_data['email']
            )
            ev_data.save()
            email_thread = threading.Thread(target=booking_email, args=(ev_data, ev_data.email,'evCharger'))
            email_thread.start()
            return redirect('/')
    else:
        form = EVChargerForm()
    return render(request, 'forms/EV_Charger_Form.html', {'form': form})

class HeatPumpForm(forms.Form):
    heating_type = forms.CharField()
    location_type = forms.CharField()
    ownership_type = forms.CharField()
    heat_pump_type = forms.CharField()
    duration = forms.CharField()
    property_type = forms.CharField()
    insulation = forms.CharField()
    radiators = forms.CharField()
    available_space = forms.CharField()
    power_type = forms.CharField()
    name = forms.CharField()
    full_address = forms.CharField()
    post_code = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

def HeatPumpFormView(request):
    if request.method == 'POST':
        form = HeatPumpForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            heat_pump_data = Q_HeatPumps(
                heating_type=cleaned_data['heating_type'],
                location_type=cleaned_data['location_type'],
                ownership_type=cleaned_data['ownership_type'],
                heat_pump_type=cleaned_data['heat_pump_type'],
                duration=cleaned_data['duration'],
                property_type=cleaned_data['property_type'],
                insulation=cleaned_data['insulation'],
                radiators=cleaned_data['radiators'],
                available_space=cleaned_data['available_space'],
                power_type=cleaned_data['power_type'],
                name=cleaned_data['name'],
                full_address=cleaned_data['full_address'],
                post_code=cleaned_data['post_code'],
                phone=cleaned_data['phone'],
                email=cleaned_data['email']
            )
            heat_pump_data.save()
            email_thread = threading.Thread(target=booking_email, args=(heat_pump_data, heat_pump_data.email,'heatpump'))
            email_thread.start()
            return redirect('/')
    else:
        form = HeatPumpForm()
    return render(request, 'forms/Heat_Pump_Form.html', {'form': form})

class HomeSecurityForm(forms.Form):
    ownership = forms.CharField()
    residency = forms.CharField()
    age_of_building = forms.CharField()
    number_of_floors = forms.CharField()
    square_footage = forms.CharField()
    number_of_people = forms.CharField()
    average_age = forms.CharField()
    usual_stay = forms.CharField()
    name = forms.CharField()
    full_address = forms.CharField()
    post_code = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

def HomeSecurityView(request):
    if request.method == 'POST':
        form = HomeSecurityForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            home_security_data = Q_HomeSecurity(
                ownership=cleaned_data['ownership'],
                residency=cleaned_data['residency'],
                age_of_building=cleaned_data['age_of_building'],
                number_of_floors=cleaned_data['number_of_floors'],
                square_footage=cleaned_data['square_footage'],
                number_of_people=cleaned_data['number_of_people'],
                average_age=cleaned_data['average_age'],
                usual_stay=cleaned_data['usual_stay'],
                name=cleaned_data['name'],
                full_address=cleaned_data['full_address'],
                post_code=cleaned_data['post_code'],
                phone=cleaned_data['phone'],
                email=cleaned_data['email']
            )
            home_security_data.save()
            email_thread = threading.Thread(target=booking_email, args=(home_security_data, home_security_data.email,'homeSecurity'))
            email_thread.start()
            return redirect('/')
    else:
        form = HomeSecurityForm()
    return render(request, 'forms/Home_Security_form.html', {'form': form})

class InfraredHeatingForm(forms.Form):
    ownership = forms.CharField()
    residency = forms.CharField()
    heating_type = forms.CharField()
    name = forms.CharField()
    full_address = forms.CharField()
    post_code = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

def InfraredHEatingView(request):
    if request.method == 'POST':
        form = InfraredHeatingForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            infrared_heating_data = Q_InfraredHeat(
                ownership=cleaned_data['ownership'],
                residency=cleaned_data['residency'],
                heating_type=cleaned_data['heating_type'],
                name=cleaned_data['name'],
                full_address=cleaned_data['full_address'],
                post_code=cleaned_data['post_code'],
                phone=cleaned_data['phone'],
                email=cleaned_data['email']
            )
            infrared_heating_data.save()
            email_thread = threading.Thread(target=booking_email, args=(infrared_heating_data, infrared_heating_data.email,'infrared'))
            email_thread.start()
            return redirect('/')
    else:
        form = InfraredHeatingForm()
    return render(request, 'forms/Infrared_heating_form.html', {'form': form,})

class SolarSystemForm(forms.Form):
    installation_type = forms.CharField()
    residency = forms.CharField()
    ownership = forms.CharField()
    solar_type = forms.CharField()
    solar_exists = forms.CharField()
    building_type = forms.CharField()
    bed_rooms = forms.CharField()
    kws_usages = forms.CharField()
    monthly_usages = forms.CharField()
    avg_electricity_bill = forms.CharField()
    roof_direction = forms.CharField()
    roof_window = forms.CharField()
    roof_shadow_impact = forms.CharField()
    pitch_type = forms.CharField()
    installation_duration = forms.CharField()
    name = forms.CharField()
    full_address = forms.CharField()
    post_code = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

def SolarSystemView(request):
    if request.method == 'POST':
        form = SolarSystemForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            solar_data = Q_Solar(
                installation_type=cleaned_data['installation_type'],
                residency=cleaned_data['residency'],
                ownership=cleaned_data['ownership'],
                solar_type=cleaned_data['solar_type'],
                solar_exists=cleaned_data['solar_exists'],
                building_type=cleaned_data['building_type'],
                bed_rooms=cleaned_data['bed_rooms'],
                kws_usages=cleaned_data['kws_usages'],
                monthly_usages=cleaned_data['monthly_usages'],
                avg_electricity_bill=cleaned_data['avg_electricity_bill'],
                roof_direction=cleaned_data['roof_direction'],
                roof_window=cleaned_data['roof_window'],
                roof_shadow_impact=cleaned_data['roof_shadow_impact'],
                pitch_type=cleaned_data['pitch_type'],
                installation_duration=cleaned_data['installation_duration'],
                name=cleaned_data['name'],
                full_address=cleaned_data['full_address'],
                post_code=cleaned_data['post_code'],
                phone=cleaned_data['phone'],
                email=cleaned_data['email']
            )
            solar_data.save()
            email_thread = threading.Thread(target=booking_email, args=(solar_data,solar_data.email,'solar'))
            email_thread.start()
            
            return redirect('/')
    else:
        form = SolarSystemForm()
    return render(request, 'forms/solar_form.html', {'form': form})

class WindowInsForm(forms.Form):
    glazing_for = forms.CharField()
    ownership = forms.CharField()
    number_of_window = forms.CharField()
    delivery = forms.CharField()
    name = forms.CharField()
    full_address = forms.CharField()
    post_code = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

def WindowInsView(request):
    if request.method == 'POST':
        form = WindowInsForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            window_ins_data = Q_Window(
                glazing_for=cleaned_data['glazing_for'],
                ownership=cleaned_data['ownership'],
                number_of_window=cleaned_data['number_of_window'],
                delivery=cleaned_data['delivery'],
                name=cleaned_data['name'],
                full_address=cleaned_data['full_address'],
                post_code=cleaned_data['post_code'],
                phone=cleaned_data['phone'],
                email=cleaned_data['email']
            )
          
            window_ins_data.save()
            email_thread = threading.Thread(target=booking_email, args=(window_ins_data,window_ins_data.email,'window_ins'))
            email_thread.start()
           
            return redirect('/')
    else:
        form = WindowInsForm()
    return render(request, 'forms/window_ins_form.html', {'form': form})

def PackagesView(request):
    packages = Packages.objects.all()
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            package_data = form.save(commit=False)
            package_data.save()
            email_thread = threading.Thread(target=booking_email, args=(package_data, package_data.email, 'package'))
            email_thread.start()
            return redirect('/')  # Redirect to desired page after form submission
    else:
        form = PackageForm()
    return render(request, 'forms/package_form.html', {'form': form, 'packages': packages})

def booking_email(form_data, email, form_type):
    subject = "Acknowledgement of Your Request for Quotation"
    from_email = "info@steuk.co.uk"
    to = [email, 'info@steuk.co.uk']  # Use the email parameter instead of string 'email'

    if form_type == 'solar':
        html_message = render_to_string('email/solar_email_template.html', {'form_data': form_data})
    elif form_type == 'window_ins':
        html_message = render_to_string('email/window_ins_email_template.html', {'form_data': form_data})
    elif form_type == 'infrared':
        html_message = render_to_string('email/infrared_email_template.html', {'form_data': form_data})
    elif form_type == 'homeSecurity':
        html_message = render_to_string('email/homeSecurity_email_template.html', {'form_data': form_data})
    elif form_type == 'heatpump':
        html_message = render_to_string('email/heatpump_email_template.html', {'form_data': form_data})
    elif form_type == 'evCharger':
        html_message = render_to_string('email/evcharger_email_template.html', {'form_data': form_data})
    elif form_type == 'boiler':
        html_message = render_to_string('email/boiler_email_template.html', {'form_data': form_data})
    else:
        # Default to a generic email template if form_type is not recognized
        html_message = render_to_string('email/package_email_template.html', {'form_data': form_data})

    plain_message = strip_tags(html_message)

    email_message = EmailMultiAlternatives(subject, plain_message, from_email, to=to)
    email_message.attach_alternative(html_message, "text/html")
    email_message.send()


