from rest_framework import viewsets
from .models import User, Frete, Motorista, Veiculo, Cnh
from .serializers import (
    UserSerializer,
    FreteSerializer,
    MotoristaSerializer,
    VeiculoSerializer,
    CnhSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FreteViewSet(viewsets.ModelViewSet):
    queryset = Frete.objects.all()
    serializer_class = FreteSerializer

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class CnhViewSet(viewsets.ModelViewSet):
    queryset = Cnh.objects.all()
    serializer_class = CnhSerializer
