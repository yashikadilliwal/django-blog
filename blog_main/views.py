from django.shortcuts import get_object_or_404, redirect, render

from about_section.models import About
from blog.models import Blog, Category
from blog_main.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    categories = Category.objects.all()

    featured_posts = Blog.objects.filter(
        is_featured=True,
        status=True   # ✅ FIXED
    ).order_by('updated_at')

    post = Blog.objects.filter(
        is_featured=False,
        status=True   # ✅ FIXED
    )

    about = About.objects.first()

    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': post,
        'about': about
    }

    return render(request, 'home.html', context)
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method=='POST':
      form=AuthenticationForm(request, request.POST)
      if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
            
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')
