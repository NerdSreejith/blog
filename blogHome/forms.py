from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content_in_short', 'Full_content', 'image']
        widgets = {
            'content': CKEditorWidget(),
        }
