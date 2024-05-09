from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, home

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
]
