from blog.models import Category

def get_categories(request):
    
    categories=Category.objects.all()
    return dict (categories=categories)

# it returns a dictionary with the key 'categories' and the value being the queryset of all Category objects. This allows you to access the categories in your templates using the variable 'categories'.