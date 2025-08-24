from rest_framework import permissions, viewsets

from .models import Events
from .serializers import EventsSerializer

class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Events to be viewed.
    adminページでの更新することを想定しているため、編集できない。
    """
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'head', 'options']