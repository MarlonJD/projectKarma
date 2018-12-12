# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import MyUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email Adress")
    name = forms.CharField(label = "Full Name")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control'})

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('email','name',)

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label="Email Adress")
    name = forms.CharField(label = "Full Name")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control'})
        
    class Meta:
        model = MyUser
        fields = ('email','name',)