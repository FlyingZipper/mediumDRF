from .models import Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name']
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'category']

    
    def validate(self, data):
        if data['name'] in ['penis', 'vagin']:
            raise serializers.ValidationError("Vulgar words")
        return data