# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import MenuPrincipal
from django.template import RequestContext
from django import forms


def menuprincipal(request):
    latest_menuprincipal_list = MenuPrincipal.objects.all()
    return render_to_response('abertura.html', {'latest_menuprincipal_list': latest_menuprincipal_list},context_instance=RequestContext(request))


