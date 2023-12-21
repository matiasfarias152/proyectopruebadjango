from rest_framework import viewsets
from .serializer import PrestamoSerializer
from .models import Prestamo

class PrestamoView(viewsets.ModelViewSet):
    serializer_class = PrestamoSerializer
    queryset = Prestamo.objects.all()