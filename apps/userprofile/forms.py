from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userprofile

class UserprofileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserprofileForm, self).__init__(*args, **kwargs)

        self.fields['address'].widget.attrs['class'] = 'input'
        self.fields['zipcode'].widget.attrs['class'] = 'input'
        self.fields['place'].widget.attrs['class'] = 'input'
        self.fields['phone'].widget.attrs['class'] = 'input'

    class Meta:
        model = Userprofile
        fields = '__all__'
        exclude = ('user', )

class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Usuário'}))
    email = forms.CharField(required=True, max_length=255, widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmação de senha'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['email'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
