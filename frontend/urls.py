
from django.urls import path
from . views import *

urlpatterns = [
    path('', Home, name="index"),
    path('shop/', Shop, name="shop"),
    path('product_list/<int:category_id>', ProductList, name="product_list"),
    path('product-details/<int:pk>', ProductDetails, name="product-details"),
    path('about-us/', About, name="about"),
    path('packages/', Package, name="packages"),
    path('package_deatils/<int:pk>', PackageDeatils, name="package_deatils"),
    path('services/', AllServices, name="services"),
    path('single_services/<int:pk>', SingleServices, name="single_services"),
    path('single_service_details/<int:pk>', SingleServiceDetails, name="single_service_details"),
    path('design/', Design, name="design"),
    path('installation/', Installation, name="installation"),
    path('maintenance/', Maintenance, name="maintenance"),
    path('blog/', BlogView, name="blog"),
    path('blog-details/<int:pk>', BlogDetailsView, name="blog-details"),
    path('contact-us/', ContactUs, name="contact"),
    path('thanks/', Thanks, name="thanks"),

    path('admin-view/', AdminView, name="admin-view"),

    path('formItems/', formItems, name="formItems"),
   # path('form_type_q/<int:pk>/', QFormType, name="form_type_q"),
    path('boiler_form/', BoilerFormView, name="boiler_form"),
    path('ev_charger_form/', EVChargerFormView, name="ev_charger_form"),
    path('heat_pump_form/', HeatPumpFormView, name="heat_pump_form"),
    path('home_security_form/', HomeSecurityView, name="home_security_form"),
    path('infrared_heating_form/', InfraredHEatingView, name="infrared_heating_form"),
    path('solar_form/', SolarSystemView, name="solar_form"),
    path('window_form/', WindowInsView, name="window_form"),
    path('package_form/', PackagesView, name="package_form"),

    
]
  