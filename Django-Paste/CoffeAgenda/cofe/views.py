from django.shortcuts import render
from cofe.models import Envento

# Create your views here.


def lista_eventos(request):
    usuario = request.user
    evento = Envento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render (request, 'agenda.html',dados)