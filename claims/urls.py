from django.urls import path
from . views import *

app_name = 'claims'

urlpatterns = [
    path('', ClaimsListView.as_view(), name='claims'),
    path('details/<pk>/', ClaimsDetailView.as_view(), name='details'),
    path('create/', ClaimsCreateView.as_view(), name='create'),
    path('update/<pk>/', ClaimsUpdateView.as_view(), name='update'),
    path('delete/<pk>/', ClaimsDeleteView.as_view(), name='delete'),
]