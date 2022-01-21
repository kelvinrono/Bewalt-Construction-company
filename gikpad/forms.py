from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Clientrequest
# from django.forms.fields import ChoiceField
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clientrequest
        fields = ('name', 'email','phone','message')
        labels = {
            
           
        }
        widget=forms.RadioSelect
       