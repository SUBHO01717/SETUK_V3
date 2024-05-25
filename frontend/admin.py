from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Brochure)
admin.site.register(Blog)
admin.site.register(Contact)

admin.site.register(ServiceCategory)
admin.site.register(Services)
admin.site.register(PackageCatgory)
admin.site.register(Packages)

admin.site.register(Q_BoilerData)
admin.site.register(Q_EVData)
admin.site.register(Q_HeatPumps)
admin.site.register(Q_HomeSecurity)
admin.site.register(Q_InfraredHeat)
admin.site.register(Q_Solar)
admin.site.register(Q_Window)
admin.site.register(Q_Packages)

admin.site.register(Jobs)
admin.site.register(JobApplication)


