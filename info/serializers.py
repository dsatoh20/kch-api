from rest_framework import serializers
from .models import Info


class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
