from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pessoa
from .serializers import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    @action(detail=True, methods=['get'])
    def peso_ideal(self, request, pk=None):
        pessoa = self.get_object()
        if pessoa.sexo.lower() == 'masculino':
            peso_ideal = (72.7 * pessoa.altura) - 58
        else:
            peso_ideal = (62.1 * pessoa.altura) - 44.7
        return Response({'peso_ideal': round(peso_ideal, 2)})
    


def index(request):
    return render(request, 'index.html')