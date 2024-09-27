from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.urls.base import resolve

from actions.views import UserLoginView, PublicKeyView, clear_link


class StructureURLsTest(TestCase):
    """ Тестируем URLs """

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='12345')

    # тест url ''
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve(reverse('actions:login'))
        self.assertEqual(found.func.view_class, UserLoginView)

    def test_homepage_url(self):
        response = self.client.get(reverse('actions:login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # тест url 'public-key/'
    def test_root_url_resolves_to_public_key_view(self):
        found = resolve(reverse('actions:public_key'))
        self.assertEqual(found.func.view_class, PublicKeyView)

    def test_public_key_url_as_authorized_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('actions:public_key'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # тест url 'clear-search/'
    def test_root_url_resolves_to_clear_search(self):
        found = resolve(reverse('actions:clear_link'))
        self.assertEqual(found.func, clear_link)
