from django.urls import path
from .views import home, vista_vehiculos, form_vehiculo


urlpatterns = [
    path('', home, name='home'),
    path('vehiculo', vista_vehiculos,name="vehiculos"),
    path('form_vehiculo', form_vehiculo, name="form_vehiculo"),
]

