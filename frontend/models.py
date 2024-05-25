from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255,null=True, blank=True)
    images=models.ImageField(upload_to='media/category',null=True, blank=True)

    def __str__(self): 
        return self.name
    
class Brand(models.Model):
    brand_name=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.brand_name
    
class Product(models.Model):
    SHOW=[("YES", "YES"),('No','No')]
    name = models.CharField(max_length=255, null=True, blank=True)
    regular_price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,default=None)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE, default=None)
    short_description=RichTextUploadingField(null=True, blank=True)
    product_overview=RichTextUploadingField(null=True, blank=True)
    product_specifcation=RichTextUploadingField(null=True, blank=True)
    show_product= models.CharField(choices=SHOW, max_length=3, default="YES")
    created_at = models.DateField(default=timezone.now)
   

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='media/product')

    def __str__(self):
        return self.product.name


def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(_('Only PDF files are allowed.'))
    

class Brochure(models.Model):
    product = models.ForeignKey(Product, related_name='brochure', on_delete=models.CASCADE, default=None)
    file = models.FileField(upload_to='media/brochures', validators=[validate_pdf])
    def __str__(self):
        return self.product.name
    
class Blog(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='media/blog',blank=True,null=True)
    source=models.CharField(max_length=255, null=True,blank=True)
    details=RichTextUploadingField(null=True, blank=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"
    

class Contact(models.Model):
    full_name=models.CharField(max_length=255)
    email=models.EmailField()
    contact_number=models.CharField(max_length=50)
    message=models.TextField()
    created_at = models.DateField(default=timezone.now)
    

    def __str__(self):
        return f"{self.full_name}"
    

class ServiceCategory(models.Model):
    image=models.ImageField(upload_to='media/service',blank=True,null=True)
    service_category_name=models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.service_category_name}"
    
class Services(models.Model):
    image=models.ImageField(upload_to='media/service',blank=True,null=True)
    category=models.ForeignKey(ServiceCategory,related_name='services', on_delete=models.CASCADE, default=None)
    service_name=models.CharField(max_length=255, blank=True, null=True)
    details=RichTextUploadingField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.service_name}"
    
class PackageCatgory(models.Model):
    package_category_name=models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.package_category_name}"
    
class Packages(models.Model):
    image=models.ImageField(upload_to='media/packages',blank=True,null=True)
    category=models.ForeignKey(PackageCatgory,related_name='packages', on_delete=models.CASCADE, default=None)
    package_name=models.CharField(max_length=255, blank=True, null=True)
    package_summary=RichTextUploadingField(null=True, blank=True)
    package_details=RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return f"{self.package_name}"
    
class Projects(models.Model):
    image=models.ImageField(upload_to='media/projects',blank=True,null=True)
    package_name=models.CharField(max_length=255, blank=True, null=True)
    details=RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return f"{self.package_name}"
    
class Q_BoilerData(models.Model):
     property_type=models.CharField(max_length=255,)
     job_type=models.CharField(max_length=255,)
     boiler_type=models.CharField(max_length=255, )
     power_usage=models.CharField(max_length=255,)
     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255,)
     post_code=models.CharField(max_length=255,)
     phone=models.CharField(max_length=255,)
     email=models.EmailField()

     def __str__(self):
         return f"{self.name}"
    
class Q_EVData(models.Model):
     installation_type=models.CharField(max_length=255)
     ownership_type=models.CharField(max_length=255)
     parking_type=models.CharField(max_length=255)
     car_type=models.CharField(max_length=255)
     charger_type=models.CharField(max_length=255)
     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255)
     post_code=models.CharField(max_length=255)
     phone=models.CharField(max_length=255)
     email=models.EmailField()

     def __str__(self):
         return f"{self.name}"

class Q_HeatPumps(models.Model):
     heating_type=models.CharField(max_length=255 )
     loaction_type=models.CharField(max_length=255 )
     owenership_type=models.CharField(max_length=255)
     heat_pump_type=models.CharField(max_length=255)
     duration=models.CharField(max_length=255)
     property_type=models.CharField(max_length=255)
     insulation=models.CharField(max_length=255)
     radiators=models.CharField(max_length=255)
     avilable_space=models.CharField(max_length=255)
     power_type=models.CharField(max_length=255)

     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255)
     post_code=models.CharField(max_length=255)
     phone=models.CharField(max_length=255)
     email=models.EmailField()
     def __str__(self):
         return f"{self.name}"
    
class Q_HomeSecurity(models.Model):
     ownership=models.CharField(max_length=255)
     residency=models.CharField(max_length=255)
     age_of_building=models.CharField(max_length=255)
     number_of_floors=models.CharField(max_length=255)
     square_footage=models.CharField(max_length=255)
     number_of_people=models.CharField(max_length=255)
     average_age=models.CharField(max_length=255)
     usual_stay=models.CharField(max_length=255)

     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255)
     post_code=models.CharField(max_length=255)
     phone=models.CharField(max_length=255)
     email=models.EmailField() 

     def __str__(self):
         return f"{self.name}"

class Q_InfraredHeat(models.Model):
     ownership=models.CharField(max_length=255)
     residency=models.CharField(max_length=255)
     heating_type=models.CharField(max_length=255)
     
     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255)
     post_code=models.CharField(max_length=255)
     phone=models.CharField(max_length=255)
     email=models.EmailField()

   

     def __str__(self):
         return f"{self.name}"
     
class Q_Solar(models.Model):
     installation_type=models.CharField(max_length=255)
     residency=models.CharField(max_length=255)
     ownership=models.CharField(max_length=255)
     solar_type=models.CharField(max_length=255)
     solar_exists=models.CharField(max_length=255)
     building_type=models.CharField(max_length=255)
     bed_rooms=models.CharField(max_length=255)
     kws_usages=models.CharField(max_length=255)
     monthly_usages=models.CharField(max_length=255)
     avg_electricity_bill=models.CharField(max_length=255)
     roof_direction=models.CharField(max_length=255)
     roof_window=models.CharField(max_length=255)
     roof_shadow_impact=models.CharField(max_length=255)
     pitch_type=models.CharField(max_length=255)
     installation_duration=models.CharField(max_length=255)
     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255, null=True, blank=True)
     post_code=models.CharField(max_length=255, null=True, blank=True)
     phone=models.CharField(max_length=255, null=True, blank=True)
     email=models.EmailField(null=True, blank=True)
     def __str__(self):
         return f"{self.name}"
     
class Q_Window(models.Model):
     glazing_for=models.CharField(max_length=255)
     ownership=models.CharField(max_length=255 )
     number_of_window=models.CharField(max_length=255 )
     delivery=models.CharField(max_length=255 )

     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255, null=True, blank=True)
     post_code=models.CharField(max_length=255, null=True, blank=True)
     phone=models.CharField(max_length=255, null=True, blank=True)
     email=models.EmailField(null=True, blank=True)
     def __str__(self):
         return f"{self.name}"

class Q_Packages(models.Model):
    pack_name=models.ForeignKey(Packages,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    full_address=models.CharField(max_length=255, null=True, blank=True)
    post_code=models.CharField(max_length=255, null=True, blank=True)
    phone=models.CharField(max_length=255, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    
    def __str__(self):
         return f"{self.name}"
    

class Jobs(models.Model):
    title=models.CharField(max_length=255, null=True, blank=True)
    job_requirements=RichTextUploadingField(null=True, blank=True)
    job_resposiblities=RichTextUploadingField(null=True, blank=True)
    job_post_date=models.DateField()
    application_deadline=models.DateField()
    
    def __str__(self):
        return f'{self.title}'
    

class JobApplication(models.Model):
    post=models.ForeignKey(Jobs, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    contact_number=models.CharField(max_length=255)
    about=models.TextField()
    indentification_card=models.FileField(upload_to='media/application',blank=True,null=True)
    cv=models.FileField(upload_to='media/application',blank=True,null=True)
    certificates=models.FileField(upload_to='media/application',blank=True,null=True)

    def __str__(self):
        return f"{self.full_name} - {self.post}"
