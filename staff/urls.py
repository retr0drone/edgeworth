from django.urls import path
from . views import *

app_name = 'staff'

urlpatterns = [
    path('client-claims', ClaimsListView.as_view(), name='client-claims'),
    path('claim-details/<pk>/', ClaimsDetailView.as_view(), name='claim-details'),
    path('create-claim/', ClaimsCreateView.as_view(), name='create-claim'),
    path('update-claim/<pk>/', ClaimsUpdateView.as_view(), name='update-claim'),
    path('delete-claim/<pk>/', ClaimsDeleteView.as_view(), name='delete-claim'),
]