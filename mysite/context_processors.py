from .models import Category

def category_names(request):
    categories = Category.objects.all()
    return {'categories' : categories}

