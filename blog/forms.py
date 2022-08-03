from django import forms
from .models import Post
class CreateUserForms(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password1 = forms.CharField(max_length=150)
    password2 = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    
    
class PostModelForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['titulo', 'texto', 'data','imagem', 'usuario']
    