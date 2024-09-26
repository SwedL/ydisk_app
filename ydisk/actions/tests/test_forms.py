from django.test import SimpleTestCase

from actions.forms import UserLoginForm, LinkForm


class UserLoginFormTest(SimpleTestCase):
    """ Тест формы авторизации пользователя """

    def setUp(self):
        self.form = UserLoginForm()

    def test_form_field_label(self):
        # Проверка наименования полей формы
        self.assertTrue(
            self.form.fields['username'].label is None or self.form.fields['username'].label == 'Логин')
        self.assertTrue(
            self.form.fields['password'].label is None or self.form.fields['password'].label == 'Пароль')

    def test_user_form_validation_for_blank_items(self):
        # Проверка невалидных данных формы
        form = UserLoginForm(data={'username': '', 'password': ''})
        self.assertFalse(form.is_valid())


class LinkFormTest(SimpleTestCase):
    """ Тест формы публичной ссылки """

    def setUp(self):
        self.form = LinkForm()

    def test_form_field_label(self):
        # Проверка наименования полей формы
        self.assertTrue(
            self.form.fields['public_key'].label is None or self.form.fields['public_key'].label == 'public_key')
