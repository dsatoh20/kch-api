from django.urls import include, path
from rest_framework import routers

from .views import ClickOnLinkViewSet, dashboard

router = routers.DefaultRouter()
router.register(r'', ClickOnLinkViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('dashboard/', dashboard),
    path('', include(router.urls)),
]