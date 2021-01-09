from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *


router = DefaultRouter()

router.register('claims', ClaimsViewSet)

# customized for post method
claims_detail = ClaimsViewSet.as_view({'get': 'list', 'post': 'create'})

app_name = 'claims'

urlpatterns = [
    path('', ClaimsListView.as_view(), name='claims'),
    path('details/<pk>/', ClaimsDetailView.as_view(), name='details'),
    path('create/', ClaimsCreateView.as_view(), name='create'),
    path('update/<pk>/', ClaimsUpdateView.as_view(), name='update'),
    path('delete/<pk>/', ClaimsDeleteView.as_view(), name='delete'),

    # Django Rest Framework

    # Router
    path('', include(router.urls)),
    path('detail/', claims_detail, name='detail'), # customized for post method url
]