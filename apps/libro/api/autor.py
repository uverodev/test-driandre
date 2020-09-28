from apps.libro.models import Autor, Libro
from apps.libro.serializers import LibroSerializer, AutorSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

class AutorListView(ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'apellidos']

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        nombre = request.GET.get("nombre")
        apellido = request.GET.get("apellido")
        if nombre and apellido:
            autores = queryset.filter(
                nombre__icontains = nombre,
                apellidos__icontains = apellido, estado = True
                ).distinct()
            
            libros = Libro.objects.filter(autor_id__in = autores.all())
            
            serializer2 = LibroSerializer(libros, many=True)
            return Response(serializer2.data)
        else:
            buscar = request.GET.get("buscar")
            if buscar:
                queryset = queryset.filter(
                    Q( nacionalidad__icontains = buscar )
                    | Q( descripcion__icontains = buscar ),
                    estado = True)
            
        
            
        serializer = AutorSerializer(queryset, many=True)

        return Response(serializer.data)


class AutorDetailView(RetrieveAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class AutorCreateView(CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class AutorUpdateView(UpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class AutorDeleteView(DestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

