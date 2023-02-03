from django import forms
from django.contrib.auth.models import User
from usuario.models import Avatar
from django.contrib.auth.forms import PasswordChangeForm

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')