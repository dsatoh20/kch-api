from rest_framework import permissions, viewsets

from .models import Info
from .serializers import InfoSerializer

class InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Info to be viewed.
    adminページでの更新することを想定しているため、編集できない。
    """
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'head', 'options']