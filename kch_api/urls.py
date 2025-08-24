from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/info/', include('info.urls')),
    path('api/v1/events/', include('events.urls')),
]