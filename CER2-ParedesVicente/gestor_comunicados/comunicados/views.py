from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Comunicado
from django.views.generic import ListView

# Create your views here.

def home(request):
    return render (request, 'comunicado/home.html')

#def lista_comunicados(request):

#    comunicados = Comunicado.objects.all()
#    return render(request, 'comunicados/lista_comunicados.html',{'comunicados':comunicados})

def detalle_comunicado(request, comunicado_id):
    comunicado = Comunicado.objects.get(id=comunicado_id)
    return render(request, 'comunicados/detalle_comunicado.html',)

class ComunicadoLisView(ListView):
    model=Comunicado
    template_name = 'comunicados/lista_comunicados.html'
    context_object_name = 'comunicados'
    orden = ['-fecha']

    def get_queryset(self):
        QuerySet= super().get_queryset()
        nivel = self.request.GET.get('nivel')
        categoria = self.request.GET.get('categoria')

        if nivel:
            QuerySet= QuerySet.filter(nivel=nivel)

        if categoria:
            QuerySet = QuerySet.filter(categoria_nombre=categoria)

        return QuerySet
    