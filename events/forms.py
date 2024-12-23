from django import forms
from events.models import User,Events
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    
    class Meta:
        
        model = User

        fields = ["username","email","phone","password1","password2",]
        
class SignInForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput)

    password = forms.CharField(widget=forms.PasswordInput)

class EventForm(forms.ModelForm):
    
    class Meta:
        
        model = Events

        fields = ["title","description","event_date","event_time","location"]
