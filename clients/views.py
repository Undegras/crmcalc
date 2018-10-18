from django.template import loader, Context
from django.http import HttpResponse
from .models import *
from django.shortcuts import render
from django.utils import timezone
from .forms import Clients


def clientslist(request):
    clientslist = Clients.objects.all()
    template = loader.get_template('clients.html')
    context = {
        'clientslist': clientslist,
        }

    return HttpResponse(template.render(context))

def post_list(request):
    return render(request, 'post_list.html', {})

def index(request):
    clients = Clients.objects.all()
    #clients.pagename = Clients.get_model_fields(Clients)
    pagename = Clients.get_model_name(Clients)

    return render(request, "clients.html", {"clients": clients, "pagename": pagename })
