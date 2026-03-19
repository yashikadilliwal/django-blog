from django.db import models


# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title
    

class Social_links(models.Model):
    platform=models.CharField(max_length=100)
    link=models.URLField()

    def __str__(self):
        return self.platform