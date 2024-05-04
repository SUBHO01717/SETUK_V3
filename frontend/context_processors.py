from .models import Category, ServiceCategory, Services

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

def service_cat_menu(request):
    service_categories = ServiceCategory.objects.all()
    return {'service_categories': service_categories}

