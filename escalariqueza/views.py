from django.http import HttpResponse

def home(*args, **kwargs):
    return HttpResponse("<h1>Home Page<h1>")

def index(request):
    return HttpResponse("Escala de Riqueza no Brasil")