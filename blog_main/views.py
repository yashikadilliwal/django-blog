from django.shortcuts import get_object_or_404, render

from about_section.models import About
from blog.models import Blog, Category


def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True , status='True').order_by('updated_at')
    post=Blog.objects.filter(is_featured=False, status='True')
    about=get_object_or_404(About, id=1)
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'post': post,
        'about': about
    }
    return render(request, 'home.html', context)