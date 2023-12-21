from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from biblioteca import views 

router = routers.DefaultRouter()
router.register(r'libros', views.LibroView, 'Libros')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]