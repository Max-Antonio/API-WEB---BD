from django.http import JsonResponse
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(responses=UsuarioSerializer)
@api_view(['GET', 'POST']) #requisições
def usuario_lista(pedido):
    #pega todos os usuários, serializa eles e retorna json
    if pedido.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse({"usuarios" : serializer.data})
    if pedido.method == 'POST':
        serializer = UsuarioSerializer(data=pedido.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@extend_schema(responses=UsuarioSerializer)
@api_view(['GET'])
def usuario_detalhe(pedido, id):
    try:
        usuario = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if pedido.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)