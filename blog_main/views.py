from django.shortcuts import render

from blog.models import Blog, Category


def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True , status='True').order_by('updated_at')
    post=Blog.objects.filter(is_featured=False, status='True')
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'post': post
    }
    return render(request, 'home.html', context)