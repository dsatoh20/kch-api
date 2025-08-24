from rest_framework import serializers
from .models import ClickOnLink


class ClickOnLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClickOnLink
        fields = '__all__'
