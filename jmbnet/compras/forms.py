from jmbnet.compras.models import *
from django.forms import *

class ClienteForm(ModelForm):
  data_nascimento = DateField(widget=DateTimeInput(format='%d/%m/%Y'))
  class Meta:
     model = Cliente

'''
wid_nome = TextInput(attrs={'onBlur': mark_safe("alert('Exemplo widget')")})
wid_cpf =  TextInput(attrs={'style':"width:135px;",})
class ClienteForm(ModelForm):
  nome = CharField(max_length=200,widget=wid_nome)
  cpf = CharField(widget=wid_cpf)
  class Meta:
     model = Cliente
'''
