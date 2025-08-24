from rest_framework import permissions, viewsets

from .models import Clubs
from .serializers import ClubsSerializer

class ClubsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Clubs to be viewed.
    adminページでの更新することを想定しているため、編集できない。
    """
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'head', 'options']