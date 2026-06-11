from django.urls import path
#
from . import views
#
app_name = 'users_app'

urlpatterns = [
    path('crear-usuario', views.CrearUsuarioView.as_view(), name='crear_usuario'),
    path('login-usuario', views.UserLoginView.as_view(), name='login_usuario'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('actualizar-password', views.ActualizarPasswordView.as_view(), name='actualizar_password'),
    path('verificar-codigo/<pk>/', views.VerificarCodigoView.as_view(), name='verificar_codigo'),
]
