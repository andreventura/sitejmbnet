# CreaesponseRedirecthere.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django import forms
from django.contrib.auth.decorators import login_required
from jmbnet.compras.models import *
from jmbnet.compras.forms import *
 
def compras(request):
  return render_to_response('compras.html', locals(),context_instance=RequestContext(request)) 

def insert(request):
  clienteform = ClienteForm()
  clientes = Cliente.objects.all()
  bairros = Bairro.objects.all()
  logradouros = Logradouro.objects.all()
  return render_to_response('clienteform.html',
      {'form':clienteform,
       'clientes':clientes,
       'bairros':bairros,
       'logradouros':logradouros,
       'operacao':'Cadastrar',
      },
      context_instance=RequestContext(request))

'''
Exibe os clientes cadastrados e um formulario para cadastrar novo cliente. 
Na realidade o template exibido eh o clienteform que por sua vez extende o template clientes.html 
resultando na exibicao dos 2 ao mesmo tempo.
'''
def list(request):
  clienteform = ClienteForm()
  clientes = Cliente.objects.all()
  bairros = Bairro.objects.all()
  return render_to_response('clienteform.html',{
      'form':clienteform,
      'clientes':clientes,
      'bairros':bairros,
      'operacao':'Cadastrar',
      })


'''
Cadastra os dados do cliente no banco de dados.
'''
from django.http import HttpResponse
def add(request):
  if request.method == 'POST':
     clienteform = ClienteForm(request.POST)
     if clienteform.is_valid():
        clienteform.save()
        mensagem = 'Cadastro realizado com sucesso.'
     else:
        mensagem = 'Erro na validacao do form.'
     
     clientes = Cliente.objects.all()
     operacao = 'Cadastrar'
     return render_to_response('clienteform.html',{
	   'form':clienteform,
	   'clientes':clientes,
	   'mensagem':mensagem,
	   'operacao':operacao
	   })
  else:
       return HttpResponse("Nao foi submetido nenhum formulario.")


'''
Remove o cliente do banco de dados a partir do id fornecido.
'''
def delete(request):
  if request.method == 'POST':
     id = request.POST.get('listaclientes')
     if id > 0:
        Cliente.objects.get(pk=id).delete()
        return HttpResponseRedirect('/cliente/list/')
     else:
        return HttpResponse("Nenhum cliente foi selecionado. Id=0.")
  else:
     return HttpResponse("Nao foi submetido nenhum formulario.")


'''
Obtem os dados do cliente a partir do id fornecido e preenche o formulario usado no cadastro.
'''
def edit(request):
  if request.method == 'POST':
     id = request.POST.get('listaclientes')
     if id > 0:
        clientes = Cliente.objects.get(pk=id)      
        clienteform = ClienteForm(instance=clientes)
        form_url = '/cliente/update/'
        # operacao = 'Atualizar'
	# raise Exception(operacao)
	operacao = 'Cadastrar'
        return render_to_response('clientes.html', {
	       'form':clienteform,
	       'id_cliente':id,
	       'form_url':form_url,
	       'operacao':operacao
	       })
     else:
        return HttpResponse("Nenhum cliente foi selecionado. id=0.")
  else:
     return HttpResponse("Nao foi submetido nenhum formulario.")


'''
Atualiza os dados do cliente e tenta fazer a validacao do mesmo jeito que o metodo add.
'''
def update(request):
  if request.method == 'POST':
     id = request.POST.get('id')
     if id > 0:
        cliente = Cliente.objects.get(pk=id)
        clienteform = ClienteForm(request.POST,instance=cliente)
        if clienteform.is_valid():
           clienteform.save()
           return HttpResponseRedirect('/cliente/list/')
        else:
           mensagem = 'erro'
           operacao = 'Atualizar'
           return render_to_response('clienteform.html',{'form':clienteform, 'mensagem':mensagem, 'id_cliente':id, 'operacao':operacao})
     else:
           return HttpResponse("Nenhum cliente foi selecionado. id=0.")
  else:
     return HttpResponse("Nao foi submetido nenhum formulario.")



#A partir da palavra-chave fornecida, eh feita uma busca case-insensitive
#na tabela cliente nos campos nome e cpf. Equivalente em SQL a WHERE nome LIKE OR cpf LIKE 
#Para tal tarefa vamos utilizar o objeto Q, pertecente a biblioteca django.db.models.

def search(request):
  if request.method == 'POST':
     palavra = request.POST.get('busca')
     if len(palavra) > 0:
        from django.db.models import Q
	clientes = Cliente.objects.filter(Q(nome__icontains=palavra) | Q(cpf__icontains=palavra))
	bairros = Bairro.objects.all()
	clienteform = ClienteForm()
	return render_to_response('clienteform.html',{
	                          'form':clienteform,
			          'clientes':clientes,
			          'bairros':bairros,
			          'operacao':'Cadastrar',
			          'titulo':'RESULTADO DA BUSCA'
			      })
     else:
        return HttpResponse("Nao foi digitado nada no campo de busca.")
  else:
        return HttpResponse("O formulario nao foi submetido.")

'''
Quando for selecionado um bairro, sera disparado o evento onchange(), chamando a funcao comboAjax(), 
que enviara uma requisicao a view /cliente/getlogradouros, 
que por sua vez fara uma consulta ao banco de dados retornando 
todos os logradouros a partir do id do bairro fornecido e 
exibindo o resultado no elemento select com id='id_logradouro'.
'''
from django.core import serializers
from django.utils import simplejson
 
def getlogradouros(request):
  if request.method == 'POST':
     id = request.POST.get('id');
     lista = Logradouro.objects.filter(bairro=id)
     if lista.count() > 0:
	html_option = ""
	for x in lista:
	   html_option += "<option>"+ str(x) +"</option>"
	dc ={}
	dc['html']=html_option
	lt=[]
	lt.append(dc)
     else:
        lista = [{"pk":"0","fields":{'logradouro':"Nenhum registro"}}]
        json = simplejson.dumps(lista)
     lista = dc
     json = simplejson.dumps(lista)
     return HttpResponse(json,mimetype="application/json")
getlogradouros = login_required(getlogradouros)

