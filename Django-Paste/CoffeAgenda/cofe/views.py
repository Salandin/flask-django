from django.shortcuts import render, redirect
from cofe.models import Envento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse
# Create your views here.
def login_users(request):
    return render (request, 'login.html')

def tchau_user(request):
    logout(request)
    return redirect('/')

def submit_users(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,"Tudo errado isso aí meu bom")

    return redirect('/')

@login_required(login_url='/login')

def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Envento.objects.filter(usuario=usuario,
                                    date_event__gt = data_atual)
    dados = {'eventos':evento}
    return render (request, 'agenda.html',dados)

@login_required(login_url='/login')
def create(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Envento.objects.get(id=id_evento)
    return render(request,'makecoffe.html', dados)

@login_required(login_url='/login')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get("titulo")
        data_evento = request.POST.get("date_event")
        descrição = request.POST.get("descrição")
        usuario = request.user
        id_evento = request.POST.get("id_evento")
        if id_evento:
            Envento.objects.filter(id=id_evento).update(titulo=titulo,
                                                        date_event=data_evento,
                                                        descrição=descrição)
        else:
            Envento.objects.create(titulo=titulo,
                                   date_event=data_evento,
                                   descrição=descrição,
                                   usuario=usuario)
    return redirect('/')
@login_required(login_url='/login')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Envento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

@login_required(login_url='/login')
def lista(request):
    usuario = request.user
    evento = Envento.objects.all().values('id','titulo')

    return JsonResponse(list(evento), safe= False)
