from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import action
from rest_framework import response

class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(detail=False)
    def get_list(self, request):
        return response.Response("hi")
      
    @action(detail=True)
    def get_product(self, request, pk=None):
        pass


    @action(detail=True, methods=['post', 'delete'])
    def delete_product(self, request, pk=None):
        pass