from django.http import response
from django.shortcuts import render, HttpResponse
from core.models import Evento


def lista_eventos(request):
    # usario = request.user
    # evento = Evento.objects.filter(usuario=usario)
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
