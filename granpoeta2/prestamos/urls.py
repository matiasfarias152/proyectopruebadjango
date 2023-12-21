from django.urls import path, include
from rest_framework import routers
from prestamos import views 

router = routers.DefaultRouter()
router.register(r'prestamos', views.PrestamoView, 'Prestamos')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]