from django.http import HttpResponse

def saludo(request): #primera Vista
    return HttpResponse("Hola Mundo")

