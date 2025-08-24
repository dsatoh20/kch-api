from rest_framework import permissions, viewsets, filters, generics

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

class ClubListView(generics.ListAPIView):
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug']