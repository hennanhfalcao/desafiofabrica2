from rest_framework import serializers
from cats.models import Cat, Fact

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = [
            'id',
            'breed',
            'coat'
        ]

class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ['id', 'cat', 'fact']
