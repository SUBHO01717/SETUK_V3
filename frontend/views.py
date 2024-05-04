from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from . form import *
from django.http import HttpResponseBadRequest
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
    return render(request, 'packages.html')

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
            form.save()
            return redirect ("/thanks/")
      
    else:
         form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)

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


def BoilerFormView(request):

    if request.method == 'POST':
        property_type = request.POST.get('property_type')
        job_type = request.POST.get('job_type')
        boiler_type = request.POST.get('boiler_type')
        power_usage = request.POST.get('power_usage')
        name = request.POST.get('name')
        full_address = request.POST.get('full_address')
        post_code = request.POST.get('post_code')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        boiler_data = Q_BoilerData(
            property_type=property_type,
            job_type=job_type,
            boiler_type=boiler_type,
            power_usage=power_usage,
            name=name,
            full_address=full_address,
            post_code=post_code,
            phone=phone,
            email=email
        )
        boiler_data.save()
        return redirect('/')
    else:
        return render(request, 'forms/Biolerform.html')
    
def EVChargerFormView(request):

    if request.method == 'POST':
        installation_type = request.POST.get('installation_type')
        ownership_type = request.POST.get('ownership_type')
        parking_type = request.POST.get('parking_type')
        car_type = request.POST.get('car_type')
        charger_type = request.POST.get('charger_type')
        name = request.POST.get('name')
        full_address = request.POST.get('full_address')
        post_code = request.POST.get('post_code')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        ev_data = Q_EVData(
            installation_type=installation_type,
            ownership_type=ownership_type,
            parking_type=parking_type,
            car_type=car_type,
            charger_type=charger_type,
            name=name,
            full_address=full_address,
            post_code=post_code,
            phone=phone,
            email=email
        )
        ev_data.save()
        return redirect('/')
    else:
        return render(request, 'forms/EV_Charger_Form.html')



def HeatPumpFormView(request):

        if request.method == 'POST':

            heating_type = request.POST.get('heating_type')
            loaction_type = request.POST.get('loaction_type')
            owenership_type = request.POST.get('owenership_type')
            heat_pump_type = request.POST.get('heat_pump_type')
            duration = request.POST.get('duration')
            property_type = request.POST.get('property_type')
            insulation = request.POST.get('insulation')
            radiators = request.POST.get('radiators')
            avilable_space = request.POST.get('avilable_space')
            power_type = request.POST.get('power_type')


            name = request.POST.get('name')
            full_address = request.POST.get('full_address')
            post_code = request.POST.get('post_code')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            heat_pump_data = Q_HeatPumps(
                heating_type=heating_type,
                loaction_type=loaction_type,
                owenership_type=owenership_type,
                heat_pump_type=heat_pump_type,
                duration=duration,
                property_type=property_type,
                insulation=insulation,
                radiators=radiators,
                avilable_space=avilable_space,
                power_type=power_type,
                name=name,
                full_address=full_address,
                post_code=post_code,
                phone=phone,
                email=email
            )
            heat_pump_data.save()
            return redirect('/')
        else:
            return render(request, 'forms/Heat_Pump_Form.html')


def HomeSecurityView(request):

        if request.method == 'POST':

            ownership = request.POST.get('ownership')
            residency = request.POST.get('residency')
            age_of_building = request.POST.get('age_of_building')
            number_of_floors = request.POST.get('number_of_floors')
            square_footage = request.POST.get('square_footage')
            number_of_people = request.POST.get('number_of_people')
            average_age = request.POST.get('average_age')
            usual_stay = request.POST.get('usual_stay')


            name = request.POST.get('name')
            full_address = request.POST.get('full_address')
            post_code = request.POST.get('post_code')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            home_security_data = Q_HomeSecurity(
                ownership=ownership,
                residency=residency,
                age_of_building=age_of_building,
                number_of_floors=number_of_floors,
                square_footage=square_footage,
                number_of_people=number_of_people,
                average_age=average_age,
                usual_stay=usual_stay,

                name=name,
                full_address=full_address,
                post_code=post_code,
                phone=phone,
                email=email
            )
            home_security_data.save()
            return redirect('/')
        else:
            return render(request, 'forms/Home_Security_form.html')



def InfraredHEatingView(request):

        if request.method == 'POST':

            ownership = request.POST.get('ownership')
            residency = request.POST.get('residency')
            heating_type = request.POST.get('heating_type')
            name = request.POST.get('name')
            full_address = request.POST.get('full_address')
            post_code = request.POST.get('post_code')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            infrared_heating_data = Q_InfraredHeat(
                ownership=ownership,
                residency=residency,
                heating_type=heating_type,
            
                name=name,
                full_address=full_address,
                post_code=post_code,
                phone=phone,
                email=email
            )
            infrared_heating_data.save()
            return redirect('/')
        else:
            return render(request, 'forms/Infrared_heating_form.html')


def SolarSystemView(request):

        if request.method == 'POST':

            installation_type = request.POST.get('installation_type')
            residency = request.POST.get('residency')
            ownership = request.POST.get('ownership')
            solar_type = request.POST.get('solar_type')
            solar_exists = request.POST.get('solar_exists')
            building_type = request.POST.get('building_type')
            bed_rooms = request.POST.get('bed_rooms')
            kws_usages = request.POST.get('kws_usages')
            monthly_usages = request.POST.get('monthly_usages')
            avg_electricity_bill = request.POST.get('avg_electricity_bill')
            roof_direction = request.POST.get('roof_direction')
            roof_window = request.POST.get('roof_window')
            roof_shadow_impact = request.POST.get('roof_shadow_impact')
            pitch_type = request.POST.get('pitch_type')
            installation_duration = request.POST.get('installation_duration')
            name = request.POST.get('name')
            full_address = request.POST.get('full_address')
            post_code = request.POST.get('post_code')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            solar_data = Q_Solar(
                installation_type=installation_type,
                residency=residency,
                ownership=ownership,
                solar_type=solar_type,
                solar_exists=solar_exists,
                building_type=building_type,
                bed_rooms=bed_rooms,
                kws_usages=kws_usages,
                monthly_usages=monthly_usages,
                avg_electricity_bill=avg_electricity_bill,
                roof_direction=roof_direction,
                roof_window=roof_window,
                roof_shadow_impact=roof_shadow_impact,
                pitch_type=pitch_type,
                installation_duration=installation_duration,
            
                name=name,
                full_address=full_address,
                post_code=post_code,
                phone=phone,
                email=email
            )
            solar_data.save()
            return redirect('/')
        else:
            return render(request, 'forms/solar_form.html')



def WindowInsView(request):

        if request.method == 'POST':

            glazing_for = request.POST.get('glazing_for')
            ownership = request.POST.get('ownership')
            number_of_window = request.POST.get('number_of_window')
            delivery = request.POST.get('delivery')

            name = request.POST.get('name')
            full_address = request.POST.get('full_address')
            post_code = request.POST.get('post_code')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            window_ins_data = Q_Window(
                glazing_for=glazing_for,
                ownership=ownership,
                number_of_window=number_of_window,
                delivery=delivery,
            
                name=name,
                full_address=full_address,
                post_code=post_code,
                phone=phone,
                email=email
            )
            window_ins_data.save()
            return redirect('/')
        else:
            return render(request, 'forms/window_ins_form.html')





# def QFormType(request, pk):
#     form_type = get_object_or_404(Q_FormType, pk=pk)

#     if request.method == "POST":
#         if form_type.name == 'Boiler':
#             form = BoilerForm(request.POST)
#         elif form_type.name == 'Heat Pump':
#             form = HeatPumpForm(request.POST)
#         elif form_type.name == 'EV Charger':
#             form = EVForm(request.POST)
#         elif form_type.name == 'Home Security':
#             form = HomeSecurityForm(request.POST)

#         elif form_type.name == 'Infrared Heating':
#             form = InfraredHeatForm(request.POST)

#         elif form_type.name == 'Solar System':
#             form = SolarForm(request.POST)
        
#         elif form_type.name == 'Window':
#             form = WindowForm(request.POST)

#         else:
#             return HttpResponseBadRequest("Invalid form type")

#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         initial_values = {}
#         if form_type.name == 'Boiler':
#             initial_values = {'formType': 'Boiler'}  # Set default values for BoilerForm fields
#             form = BoilerForm(initial=initial_values)
#         elif form_type.name == 'Heat Pump':
#             initial_values = {'formType': 'Heat Pump'}  # Set default values for HeatPumpForm fields
#             form = HeatPumpForm(initial=initial_values)
#         elif form_type.name == 'EV Charger':
#             initial_values = {'formType': 'EV Charger'}  # Set default values for EVForm fields
#             form = EVForm(initial=initial_values)
        
#         elif form_type.name == 'Home Security':
#             initial_values = {'formType': 'Home Security'}  # Set default values for EVForm fields
#             form = HomeSecurityForm(initial=initial_values)

#         elif form_type.name == 'Infrared Heating':
#             initial_values = {'formType': 'Infrared Heating'}  # Set default values for EVForm fields
#             form = InfraredHeatForm(initial=initial_values)
#         elif form_type.name == 'Solar System':
#             initial_values = {'formType': 'Solar System'}  # Set default values for EVForm fields
#             form = SolarForm(initial=initial_values)

#         elif form_type.name == 'Window':
#             initial_values = {'formType': 'Window'}  # Set default values for EVForm fields
#             form = WindowForm(initial=initial_values)

#         else:
#             return HttpResponseBadRequest("Invalid form type")

#         return render(request, 'form.html', {'form': form, 'form_type': form_type})
