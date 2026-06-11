from django.urls import path
#
from . import views
#
app_name = 'home_app'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('prueba-mixin', views.PruebaMixinView.as_view(), name='mixin'),
]