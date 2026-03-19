from django.contrib import admin

# Register your models here.

from . models import About, Social_links
#  this ios to disable the add button in the admin panel for the About model, ensuring that only one instance of the About model can be created. The has_add_permission method checks the count of existing About objects and returns True if there are none, allowing the user to add a new About instance. If there is already an About instance, it returns False, preventing the addition of more instances.

class AboutAdmin(admin.ModelAdmin):
   
   def has_add_permission(self, request):
      count=About.objects.all().count()
      if count==0:
         return True    
      else:
         return False
      

admin.site.register(About, AboutAdmin)
admin.site.register(Social_links)