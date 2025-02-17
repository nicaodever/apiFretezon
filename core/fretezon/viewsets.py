from rest_framework import viewsets
from .models import Frete, Motorista
from .serializers import FreteSerializer, MotoristaSerializer


class FreteViewSet(viewsets.ModelViewSet):
    queryset = Frete.objects.all()
    serializer_class = FreteSerializer
    ordering_fields = '__all__'

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
    ordering_fields = '__all__'

