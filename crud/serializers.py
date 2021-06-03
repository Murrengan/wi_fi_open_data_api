from rest_framework import serializers

from crud.models import WiFiSpot


class WiFiSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiFiSpot
        fields = '__all__'
