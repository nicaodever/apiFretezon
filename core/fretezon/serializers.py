from rest_framework import serializers
from .models import User, Frete, Motorista, Veiculo, Cnh


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'name', 'email', 'phone')

    def create(self, validated_data):

        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class FreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frete
        fields = '__all__'


class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'


class CnhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnh
        fields = '__all__'
