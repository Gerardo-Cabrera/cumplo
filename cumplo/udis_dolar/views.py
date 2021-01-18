from django.shortcuts import render
from django.http import JsonResponse
from .models import Consulta
import requests


def index(request):
    data = {}

    if request.method == "POST":
        datos = {'fechaInicial': request.POST.get("fechaInicial"), 'fechaFinal': request.POST.get("fechaFinal")}
        consulta = Consulta()
        data = consulta.obtenerInformacion(datos)
        return JsonResponse({"data": data}, status=200)
    return render(request, 'udis_dolar/index.html', data)
