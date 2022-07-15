from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from ApiDRF.permissions import IsAdminOrReadOnly
from ApiDRF.serializers import ProductSerializer
from onlineshop.models import Product, Category


class ProductViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        return Product.objects.all()[:]

    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})