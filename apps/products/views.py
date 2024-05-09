from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if 'top' in self.request.query_params:
            return Product.objects.filter(top=self.request.query_params['top'] == 'true')
        return super().get_queryset()


def home(request):
    return render(request, 'home/index.html')
