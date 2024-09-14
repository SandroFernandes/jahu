from rest_framework import serializers

from .models import (
    Cor,
    MarcaModelo,
    Veiculo,
    Morador,
    Lote,
    Quadra,
    Residencia,
    Visitantes,

)


class CorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cor
        fields = '__all__'


class MarcaModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaModelo
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'


class QuadraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        fields = '__all__'


class ResidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residencia
        fields = '__all__'


class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitantes
        fields = '__all__'
