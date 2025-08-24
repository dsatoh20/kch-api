from django.http import HttpResponse
from rest_framework import viewsets
from .permissions import HasApiKeyForPost

from .models import ClickOnLink
from club.models import Clubs
from .serializers import ClickOnLinkSerializer
from django.contrib.auth.decorators import login_required

class ClickOnLinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ClickOnLink to be pushed.

    """
    queryset = ClickOnLink.objects.all()
    serializer_class = ClickOnLinkSerializer
    permission_classes = [HasApiKeyForPost]
    http_method_names = ['post', 'head', 'options']

@login_required # adminユーザのみアクセス可能
def dashboard(request):
    """
    団体ごとのクリック数を表示する
    """
    if Clubs.objects.count() != 0:
        items = [{"club": club.name, "clicks": club.clicks.count()} for club in Clubs.objects.all()]
        items = sorted(items, key=lambda x: x["clicks"], reverse=True) # 降べきの順にソート
        return HttpResponse(str(items))
    else:
        return HttpResponse("No clubs found.")