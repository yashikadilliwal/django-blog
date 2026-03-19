from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Blog, Category
from django.db.models import Q as q

# Create your views here.

def posts_by_category(request, category_id):
    posts=Blog.objects.filter(status='True', category=category_id)
    # try:
    #     category=Category.objects.get(id=category_id)

    # except :
    #     return redirect('home')
    category=get_object_or_404(Category, id=category_id)
    context={
    
        'posts': posts,
        'category': category
    }
    return render( request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog=get_object_or_404(Blog, slug=slug, status='True')
    context={
        'single_blog': single_blog
    }
    return render(request, 'blog.html', context)  

#  this is for search field in navbar
def search(request):
    keywords=request.GET.get('keyword')
    blogs=Blog.objects.filter(q(title__icontains=keywords) | q(short_description__icontains=keywords) | q(blog_body__icontains=keywords), status='True') 
    context={
        'blogs': blogs,
        'keyword': keywords
    }
    return render(request, 'search.html', context)