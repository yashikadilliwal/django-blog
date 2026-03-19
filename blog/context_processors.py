from blog.models import Category
from about_section.models import Social_links
def get_categories(request):
    
    categories=Category.objects.all()
    return dict (categories=categories)

# it returns a dictionary with the key 'categories' and the value being the queryset of all Category objects. This allows you to access the categories in your templates using the variable 'categories'.

def get_social_links(request):

    social_links=Social_links.objects.all()
    return dict(social_links=social_links)