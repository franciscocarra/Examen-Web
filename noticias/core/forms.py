from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField

class EmpleadoForm(ModelForm):
    

    captcha = ReCaptchaField()
    class Meta:
        
        model = Empleado
        fields = '__all__'
       

class TipoEmpleadoForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = TipoEmpleado
        fields = '__all__'

class GeneroForm(ModelForm):

    class Meta:
        model = Genero
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']