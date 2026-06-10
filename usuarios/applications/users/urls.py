from django.urls import path
#
from . import views
#
app_name = 'users_app'

urlpatterns = [
    path('crear-usuario', views.CrearUsuarioView.as_view(), name='crear_usuario'),
    path('login-usuario', views.UserLoginView.as_view(), name='login_usuario'),
]
