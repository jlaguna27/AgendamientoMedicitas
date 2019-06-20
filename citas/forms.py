from django import forms
from django.forms.widgets import DateInput
from .models import Citamedica, Profile, Paciente, Eps, Medico, User


class Formucitamedica(forms.ModelForm):
    class Meta:
        model = Citamedica
        fields= '__all__'


class Formuprofile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = ['user']


class Formupaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields= '__all__'


class Formueps(forms.ModelForm):
    class Meta:
        model = Eps
        fields= '__all__'


class Formumedico(forms.ModelForm):
    class Meta:
        model = Medico
        fields= '__all__'


class Formuuser(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email', 'username', 'password', 'groups', 'is_staff']

class Formuuseredit(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email']