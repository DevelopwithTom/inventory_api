# from rest_framework.response import Response
from rest_framework import viewsets
from core.models import Product
from inventory.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        request = self.request
        queryset = super().get_queryset()
        not_in_stock = request.GET.get('not_in_stock')
        available = request.GET.get('available')
        if not_in_stock:
            query = queryset.filter(quantity=0)
        elif available:
            query = queryset.exclude(quantity=0)
        else:
            query = queryset

        return query

    # def list(self, request):
    #     soldout = request.GET.get('soldout')
    #     available = request.GET.get('available')
    #     if soldout:
    #         query = self.get_queryset().filter(quantity=0)
    #     elif available:
    #         query = self.get_queryset().exclude(quantity=0)
    #     else:
    #         query = self.get_queryset()
    #     serializer = self.get_serializer(query, many=True)
    #     return Response(serializer.data)
