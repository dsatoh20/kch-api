from rest_framework import serializers
from .models import Clubs


class ClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ['id', 'details'] # clientからのClickOnLinkのPOSTを受け付けるため、自動生成されたidを含める