from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import Blog,Category
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from dashboard.forms import categoryForm, blogForm



# Create your views here.

@login_required(login_url='dashboard')
def dashboard(request): 
    total_posts=Blog.objects.all().count()
    users=User.objects.all().count()
    categories=Category.objects.all().count()
    post=Blog.objects.all()
    context={
        'total_posts':total_posts,
        'users': users,
        'categories':categories,
        'posts': post,
        
    }

    return render(request, 'dashboard/dashboard.html',context)




def users(request ):
    user=User.objects.all()
    context={
        'user':user
    }
    return render(request, 'dashboard/users.html', context)

def add_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        is_staff = True if request.POST.get('is_staff') else False
        is_superuser = True if request.POST.get('is_superuser') else False

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return redirect('users')

    return render(request, 'dashboard/add_user.html')



@login_required
def edit_user(request, id):
    # 🔒 Only superuser should edit users
    if not request.user.is_superuser:
        return redirect('dashboard')

    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')

        user.is_staff = True if request.POST.get('is_staff') else False
        user.is_superuser = True if request.POST.get('is_superuser') else False

        # 🔐 Password update (optional)
        password = request.POST.get('password')
        if password:
            user.set_password(password)   # IMPORTANT

        user.save()

        return redirect('users')

    return render(request, 'dashboard/edit_user.html', {'user': user})

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users')



@login_required

def add_post(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        short_description = request.POST.get('short_description')
        blog_body = request.POST.get('blog_body')
        feature_image = request.FILES.get('feature_image')
        status = request.POST.get('status') == 'on'
        is_featured = request.POST.get('is_featured') == 'on'

        # Get category object
        category = Category.objects.get(id=category_id)

        # Create post manually
        Blog.objects.create(
            title=title,
            category=category,
            short_description=short_description,
            blog_body=blog_body,
            feature_image=feature_image,
            status=status,
            is_featured=is_featured,
            author=request.user  
        )

        return redirect('dashboard')  # ✅ correct redirect

    return render(request, 'dashboard/add_post.html', {
        'categories': categories
    })

#===================================== categories crud operations====================
def categories(request):
    categories=Category.objects.all()
    total_categories=Category.objects.all().count()
    context = {
            
        'categories': categories,
        'total_categories':total_categories,
    }
    return render(request, 'dashboard/categories.html', context)

def add_category(request):
    if request.method == "POST":
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')  # Redirect to the dashboard or another appropriate page
    else:
        form = categoryForm()
    total_posts=Blog.objects.all().count()
    users=User.objects.all().count()
    categories=Category.objects.all().count()
    context = {
        'form': form,
        'total_posts': total_posts,
        'users': users,     
        'categories': categories,
    }
    return render(request, 'dashboard/add_categories.html', context)

def delete_category(request, id):
    category=get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categories')

def edit_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        form = categoryForm(request.POST, instance=category)  
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = categoryForm(instance=category) 

    total_posts = Blog.objects.all().count()
    users = User.objects.all().count()
    total_categories = Category.objects.all().count()

    context = {
        'form': form,
        'total_posts': total_posts,
        'users': users,
        'total_categories': total_categories,
        'category':category,
    }

    return render(request, 'dashboard/edit_categories.html', context)



# ==================================== dashboard crud=========================

def delete_post(request, id):
    post=get_object_or_404(Blog, id=id)
    post.delete()
    return redirect('dashboard')

def edit_post(request, id):
    post = get_object_or_404(Blog, id=id)
    categories = Category.objects.all()

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.category_id = request.POST.get('category')
        post.short_description = request.POST.get('short_description')
        post.blog_body = request.POST.get('blog_body')

        # checkbox handling
        post.status = True if request.POST.get('status') == 'on' else False
        post.is_featured = True if request.POST.get('is_featured') == 'on' else False

        # image update (only if new uploaded)
        if request.FILES.get('feature_image'):
            post.feature_image = request.FILES.get('feature_image')

        post.save()
        return redirect('dashboard')

    context = {
        'post': post,
        'categories': categories
    }

    return render(request, 'dashboard/edit_post.html', context)