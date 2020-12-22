from rest_framework.generics import ListAPIView
from ..bread.models import Bread
from .serializers import BreadSerializer

class BreadList(ListAPIView):
    queryset = Bread.objects.all()
    serializer_class = BreadSerializer