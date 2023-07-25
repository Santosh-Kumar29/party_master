from django.urls import path
from .views import index, party_list_create_view

urlpatterns = [
    path('', index, name='index'),
    path('party-master', party_list_create_view, name='party-list-create'),
]
