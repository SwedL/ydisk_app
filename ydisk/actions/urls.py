"""Схемы URL для actions"""

from django.urls import path

from .views import PublicKeyView, UserLoginView, clear_link, logout_user

app_name = 'actions'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('public-key/', PublicKeyView.as_view(), name='public_key'),
    path('public-key/<path:public_key>/<str:path>/', PublicKeyView.as_view(), name='public_key'),
    path('clear-link/', clear_link, name='clear_link'),
    path('logout/', logout_user, name='logout'),
]
