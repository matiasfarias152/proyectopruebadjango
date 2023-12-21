from rest_framework import viewsets
from .serializer import LibroSerializer
from .models import Libro

class LibroView(viewsets.ModelViewSet):
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()