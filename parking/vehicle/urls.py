from django.urls import path
from .views import VehicleApiView

urlpatterns =[
  
    path ('list',VehicleApiView.as_view()),
    path ('crear-vehiculo', VehicleApiView.as_view()),
    path ('actualizar-vehiculo/<int:pkid>', VehicleApiView.as_view()),

    
]