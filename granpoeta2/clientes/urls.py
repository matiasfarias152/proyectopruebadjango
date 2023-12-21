from django.urls import path, include
from rest_framework import routers
from clientes import views 

router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteView, 'Clientes')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]