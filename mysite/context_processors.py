from .models import Category


def category_names(request):
    categories = Category.objects.all()
    return {'categories': categories}


def get_current_path(request):
    return {
        'current_path': request.build_absolute_uri()
    }
