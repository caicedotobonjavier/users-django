from django.shortcuts import render, redirect
#
from django.views.generic import CreateView, FormView, View
#
from .models import User
#
from .forms import UserForm, LoginForm, ActualizarPasswordForm, VerificarCodigoForm
#
from django.urls import reverse_lazy, reverse
#
from django.contrib.auth import login, logout, authenticate
#
from django.http import HttpResponseRedirect
#
from .functions import crear_codigo
#
from django.core.mail import send_mail
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
        codigo = crear_codigo()

        usuario=User.objects.create_user(
            username,
            email,
            password,
            nombres=nombres,
            apellidos=apellidos,
            genero=genero,
            codigo=codigo
        )

        send_mail(
            subject='Código de verificación',
            message=f'Tu código es: {codigo}',
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )

        return HttpResponseRedirect(
            reverse(
                'users_app:verificar_codigo',
                kwargs={'pk': usuario.id}
            )
        )


class VerificarCodigoView(FormView):
    template_name = 'users/verficar-codigo.html'
    form_class = VerificarCodigoForm
    success_url = reverse_lazy('users_app:login_usuario')


    def get_form_kwargs(self):   
        kwargs = super(VerificarCodigoView, self).get_form_kwargs()
        kwargs['id_user'] = self.kwargs['pk']
        return kwargs


    def form_valid(self, form):
        cod = form.cleaned_data['codigo']
        id_user = self.kwargs['pk']
        User.objects.filter(id=id_user).update(is_active=True)        
        
        return super(VerificarCodigoView, self).form_valid(form)





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