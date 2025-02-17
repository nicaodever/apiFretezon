from rest_framework import serializers
from .models import Frete, Motorista

class FreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frete
        fields = '__all__'

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'