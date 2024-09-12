"""Схемы URL для actions"""

from django.urls import path

from .views import UserLoginView, FollowLinkView, clear_search

app_name = 'actions'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('public-link/', FollowLinkView.as_view(), name='public_link'),
    path('clear-link/', clear_search, name='clear_link'),
]
