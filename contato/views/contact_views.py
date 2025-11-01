from django.shortcuts import render, redirect
from contato.models import Contact
from django.http import Http404
from django.db.models import Q

# Create your views here.

def index(request):
    contatos = Contact.objects.filter(show=True).order_by('id')[0:10]

    context = {
        'contatos': contatos,
        'app_titulo': 'Agenda'
        }

    return render(
        request,
        'contato/index.html',
        context,
    )

def contato_view(request, contato_id):
    unico_contato = Contact.objects.filter(pk=contato_id).first()

    if unico_contato is None:
        raise Http404()

    context = {
        'contatos': unico_contato,
        'app_titulo': f"Contato - {unico_contato.first_name}",
        }

    return render(
        request,
        'contato/contato.html',
        context
    )

def buscar(request):
    valor_requisicao = request.GET.get('q', '').strip()
    contatos = Contact.objects\
                            .filter(show=True)\
                            .filter(Q(first_name__icontains=valor_requisicao) |\
                                     Q(last_name__icontains=valor_requisicao) |\
                                    Q(phone__icontains=valor_requisicao))\
                            .order_by('id')[0:10]
    
    # Redirecionar se nao houver valor de busca
    if valor_requisicao == '':
        return redirect('contato:index')

    context = {
        'contatos': contatos,
        'app_titulo': 'Agenda'
        }

    return render(
        request,
        'contato/index.html',
        context,
    )