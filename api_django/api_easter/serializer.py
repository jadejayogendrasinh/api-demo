from rest_framework import serializers
from .models import CardItem, GIFsItem, QuotesItem

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = ('__all__')

class GIFSerializer(serializers.ModelSerializer):
    class Meta:
        model = GIFsItem
        fields = ('__all__')

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotesItem
        fields = ('__all__')