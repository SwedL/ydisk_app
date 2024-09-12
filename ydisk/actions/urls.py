"""Схемы URL для actions"""

from django.urls import path

from .views import FollowLinkView, clear_search

app_name = 'actions'

urlpatterns = [
    path('', FollowLinkView.as_view(), name='weather_forecast'),
    path('clear-search/', clear_search, name='clear_search'),
]
