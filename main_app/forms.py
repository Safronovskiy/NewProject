from django import forms
from .models import BlogCategory, BlogPost



class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'











