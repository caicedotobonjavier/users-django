from django.shortcuts import render, redirect
#
from django.views.generic import CreateView, FormView, View
#
from .models import User
#
from .forms import UserForm, LoginForm, ActualizarPasswordForm
#
from django.urls import reverse_lazy
#
from django.contrib.auth import login, logout, authenticate
#
from django.http import HttpResponse
# Create your views here.


class CrearUsuarioView(FormView):
    template_name = 'users/crear-usuario.html'
    form_class = UserForm
    success_url = reverse_lazy('users_app:crear_usuario')



    def form_valid(self, form):

        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        nombres = form.cleaned_data['nombres']
        apellidos = form.cleaned_data['apellidos']
        genero = form.cleaned_data['genero']
        password = form.cleaned_data['password']

        User.objects.create_user(
            username,
            email,
            password,
            nombres=nombres,
            apellidos=apellidos,
            genero=genero
        )

        return super(CrearUsuarioView, self).form_valid(form)



class UserLoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:index')

    
    def form_valid(self, form):

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        login(self.request, user)


        return super(UserLoginView,self).form_valid(form)



class LogoutView(View):

    def get(self, request):
        
        logout(request)

        return redirect(
            'users_app:login_usuario'
        )



class ActualizarPasswordView(FormView):
    template_name = 'users/actualizar-contrasena.html'
    form_class = ActualizarPasswordForm
    success_url = reverse_lazy('users_app:login_usuario')


    def form_valid(self, form):

        usuario = User.objects.get(username=self.request.user)
        password = form.cleaned_data['password']
        new_password = form.cleaned_data['new_password']

        auth_user = authenticate(username=usuario, password=password)

        if auth_user:
            print('Autenticado')
            usuario.set_password(new_password)
            usuario.save()
        
        logout(self.request)

        return super(ActualizarPasswordView, self).form_valid(form)