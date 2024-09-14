from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    """ Форма авторизация пользователя """

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Password'}))

    class Meta:
        fields = ('username', 'password')


class LinkForm(forms.Form):
    """ Форма ввода публичной ссылки для просмотра файлов """

    public_key = forms.URLField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_public_key', 'placeholder': 'введите публичную ссылку'}),
        label='public_key',
    )
