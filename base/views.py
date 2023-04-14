from django.shortcuts import render
#from django.http import HttpResponse
from base.forms import ContatoForm, ReservaForm
from base.models import Contato

def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(99) 99999.9999',
        'responsavel': 'Jackson Moreira',
        'form': form,
        'sucesso': sucesso
        }    
    return render(request, 'contato.html', contexto)

def reserva_banho(request):
    sucesso = False
    if request.method == 'GET':
        form = ReservaForm()
    else:
        form = ReservaForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'nomepet': input(''),
        'telefone': input(''),
        'dia': input(''),
        'mensagem': input(''), 
        'form': form,
        'sucesso': sucesso
        }
    return render(request, 'reserva_banho.html', contexto)