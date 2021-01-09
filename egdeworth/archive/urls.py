from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import *
# Django Rest Framework
from claims.views import ClaimsRestMixinListView, ClaimsRestListView, claims_rest_list_view, claims_rest_detail_view, ClaimsRestApiListView, OwnerApiDetailView, CommentApiDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('claims/', include('claims.urls', namespace='claims')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Django Rest Framework

   # Main API path
    path('api-auth/', include('rest_framework.urls')),

    # Routers
    path('api/', include('claims.urls')),

    # Owner & Comment Hyperlinks
    path('api/claims/owner/<pk>/', OwnerApiDetailView.as_view(), name='owner-detail'),
    path('api/claims/comments/<pk>/', CommentApiDetailView.as_view(), name='comments-detail'),

    # Generic Class Based Views
    # path('api/claims/', ClaimsRestApiListView.as_view(), name='claims-list'),
    # path('api/claims/detail/<pk>/', ClaimsRestApiListView.as_view(), name='claims-detail'),
    # path('api/claims/delete/<pk>/', ClaimsRestApiListView.as_view(), name='claims-delete'),

    # Mixins
    # path('api/claims/', ClaimsRestMixinListView.as_view(), name='claims-list'), 

    # path('api/claims/', ClaimsRestListView.as_view(), name='claims-list'),
    # path('api/claims/<pk>/', ClaimsRestListView.as_view(), name='claims-list'), #pk included for 'instance' update
    # path('api/claims-list', claims_rest_list_view, name='claims-list'),
    # path('api/claim-details/<pk>/', claims_rest_detail_view, name='claim-details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)