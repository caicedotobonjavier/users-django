from django.shortcuts import render
#
from django.views.generic import CreateView, FormView
#
from .models import User
#
from .forms import UserForm, LoginForm
#
from django.urls import reverse_lazy
#
from django.contrib.auth import login, logout, authenticate
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