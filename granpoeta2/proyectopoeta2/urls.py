from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include('biblioteca.urls')),
    path('clientes/', include('clientes.urls')),
    path('prestamos/', include('prestamos.urls')),
]