from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('claims/', include('claims.urls', namespace='claims')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('profile/', ProfileView.as_view(), name='prpfile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)