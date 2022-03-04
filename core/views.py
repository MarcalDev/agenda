from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento


# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def retornaLocal(request, titulo_evento):
    evento = Evento.objects.get(titulo = titulo_evento)
    local = evento.local_evento
    return HttpResponse('O local do evento {} é no(a) {}'.format(titulo_evento, local))

def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.all()
    dados = {'eventos':eventos}
    return render(request, 'agenda.html', dados)
