from django import forms
from blog.models import Category, Blog


class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    

class blogForm(forms.ModelForm):
    class Meta:
        model=Blog 
        fields='__all__'