from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, pai):
    return HttpResponse('<h1>CONFIA QUE O {} É BRAVO NO DJANGO E PYTHON</h1>'.format(pai))

def soma(request, n, m):
    valor = int(n)+int(m)
    return HttpResponse(f'A soma é {valor}')