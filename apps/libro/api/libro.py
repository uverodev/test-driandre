from apps.libro.models import Libro
from apps.libro.serializers import LibroSerializer, AutorSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.db.models import Q

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)


class LibroListView(ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo']

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        buscar = request.GET.get("buscar")
        detalles = request.GET.get("detalles")
        if buscar: 
            if detalles:
                queryset = queryset.filter(
                    Q( tags__icontains = buscar )
                    |Q( descripcion__icontains = buscar )
                    |Q(titulo__icontains = buscar ), 
                    estado = True)[:1]
            else:
                queryset = queryset.filter(
                    Q( tags__icontains = buscar )
                    |Q( descripcion__icontains = buscar )
                    |Q(titulo__icontains = buscar ), 
                    estado = True)

        else:
            date_min = request.GET.get("date_min")
            date_max = request.GET.get("date_max")
            if date_min and date_max:
                queryset = queryset.filter(fecha_publicacion__year__range=[date_min, date_max])
        
        if not queryset:
            queryset = self.get_queryset()
            queryset = queryset.filter(estado = False)


        serializer = LibroSerializer(queryset, many=True)
        return Response(serializer.data)


class LibroDetailView(RetrieveAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class LibroCreateView(CreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class LibroUpdateView(UpdateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class LibroDeleteView(DestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer