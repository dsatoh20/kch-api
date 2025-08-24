from rest_framework import serializers
from .models import Events


class EventsSerializer(serializers.ModelSerializer):
    lastUpdated = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Events
        fields = ['owner', 'title', 'date', 'image', 'url', 'lastUpdated']
    def get_lastUpdated(self, obj):
        return int(obj.lastUpdated.strftime('%Y%m%d')) # 20250824などの数値形式で返す
    def get_date(self, obj):
        return [int(event_date.date.strftime('%Y%m%d')) for event_date in obj.date.all()]