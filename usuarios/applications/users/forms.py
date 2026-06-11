from django import forms
#
from .models import User
#
from django.contrib.auth import authenticate
#

class UserForm(forms.ModelForm):

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Ingrese la contraseña'
            }
        )
    )

    confirm_password = forms.CharField(
        label='Confirmar Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirme la contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    



    def clean(self):
        cleaned_data = super(UserForm, self).clean()

        password = self.cleaned_data['password']
        password2 = self.cleaned_data['confirm_password']

        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe contener minimo 8 digitos')

        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return cleaned_data
    


class LoginForm(forms.Form):
    
    username = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Nombre de usuario'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña de usuario'
            }
        )
    )



    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        usuario = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )

        if not usuario:
            raise forms.ValidationError('Credenciales incorrectas')
        
        return cleaned_data



class ActualizarPasswordForm(forms.Form):

    password = forms.CharField(
        label='Contraseña Actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingrese contraseña actual'
            }
        )
    )

    new_password = forms.CharField(
        label='Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingrese contraseña nueva'
            }
        )
    )