from django.http import HttpResponse
import datetime

def saludo(request): # Primera Vista
    return HttpResponse("Holaaaaaaa")

def horaActual(request):

    fechaActual = datetime.datetime.now()

    return HttpResponse(f"Hora Actual: {fechaActual}")

def calcularEdad(request,edad, agno):

    edadActual = edad
    periodo = agno-2022
    edadFutura = edadActual + periodo

    return HttpResponse(f"En el año {agno}, tendras {edadFutura}")
