from django.urls import path

from apps.products.views import home

urlpatterns = [
    path('', home, name='home'),
]
