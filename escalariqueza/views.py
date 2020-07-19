from django.http import HttpResponse


def index(request):
    return HttpResponse("Escala de Riqueza no Brasil")