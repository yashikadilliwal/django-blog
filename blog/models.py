

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.


# this is the model for category of blog post
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
    
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


STATUS_CHOICES = (
    (True, 'Published'),
    (False, 'Draft'),
)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=500)
    feature_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    blog_body = models.TextField()
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)
    is_featured = models.BooleanField(default=False)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

   

    from django.utils.text import slugify

    def save(self, *args, **kwargs):
     if not self.slug:
        base_slug = slugify(self.title) or "post"
        slug = base_slug
        counter = 1

        while Blog.objects.filter(slug=slug).exclude(id=self.id).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        self.slug = slug

     super().save(*args, **kwargs)


    




    