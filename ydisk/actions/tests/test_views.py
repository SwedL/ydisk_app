from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from actions.forms import LinkForm, UserLoginForm


class UserLoginViewTest(SimpleTestCase):
    """ Тест представления главной страницы """

    def setUp(self):
        self.url = reverse('actions:login')
        self.response = self.client.get(self.url)

    def test_view_form(self):
        # Тест на соответствие формы экземпляру UserLoginForm и наличие csrf токена
        form = self.response.context_data.get('form')
        self.assertIsInstance(form, UserLoginForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_view_content_test(self):
        # Тест на содержимое страницы
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertEqual(self.response.context_data['title'], 'Авторизация')
        self.assertTemplateUsed(self.response, 'actions/login.html')


class PublicKeyViewTest(TestCase):
    """ Тест представления работы с публичной ссылкой """

    def setUp(self):
        self.user = User.objects.create(username='test_user', password='12345')
        self.url = reverse('actions:public_key')

    def test_view_content(self):
        # Тест на содержимое страницы
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        form = response.context['form']
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['title'], 'Публичная ссылка')
        self.assertTemplateUsed(response, 'actions/public_key.html')
        self.assertIsInstance(form, LinkForm)
        self.assertIn('X', response.content.decode())
        self.assertIn('Enter', response.content.decode())
        self.assertEqual(response.status_code, HTTPStatus.OK)
