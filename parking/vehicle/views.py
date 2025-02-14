from django.shortcuts import render
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from vehicle.models import vehicle 
from .serializer import vehicle_serializer
# Create your views here.

class VehicleApiView(APIView):
    def get(sel,request,*args, **kwargs):
        lista_vehiculos=vehicle.objects.all()
        serializer_vehiculos=vehicle_serializer(lista_vehiculos,many=True)
        return Response(serializer_vehiculos.data, status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        data={
            'placa': request.data.get('placa'),
            'marca': request.data.get('marca'),
            'color_vehiculo': request.data.get('color_vehiculo'),
            'modelo': request.data.get('modelo'),


        }

        serializador = vehicle_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data,status=status.HTTP_201_CREATED)
        return  Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid):
        mivehiculo=vehicle.objets.filter(id=pkid).update(
            placa=request.data.get('placa'),
            marca=request.data.get('marca'),
            color_vehiculo=request.data.get('color_vehiculo'),
            modelo=request.data.get('modelo'),
        )
        return Response(mivehiculo, status=status.HTTP_200_OK)
