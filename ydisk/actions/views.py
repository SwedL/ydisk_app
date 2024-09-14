import os
import yadisk

from django.core.cache import cache
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import LinkForm, UserLoginForm
from common.views import PublicResource, get_public_resources


class UserLoginView(LoginView):
    """ Представление домашней страницы для авторизации пользователя """

    form_class = UserLoginForm
    template_name = 'actions/login.html'
    title = 'Авторизация'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


def logout_user(request):
    logout(request)
    return redirect('/')


class PublicKeyView(View):
    """ Представление главной страницы - получения публичной ссылки """

    title = 'Публичная ссылка'
    form_class = LinkForm
    client = yadisk.Client()

    def get(self, request, public_key: str = None, path: str = None):
        context = {
            'form': self.form_class,
            'title': self.title,
        }

        if path:
            path = path.replace('*', '/')
            public_resources, public_resources_path = get_public_resources(
                client=self.client,
                public_key=public_key,
                path=path
            )

            context = {
                'form': self.form_class(request.POST),
                'title': self.title,
                'public_resources_path': public_resources_path,
                'public_resources': public_resources,
                'public_key': public_key
            }

        return render(request, 'actions/public_link.html', context=context)

    def post(self, request, path: str = None):
        public_key = request.POST['public_key']
        public_resources, public_resources_path = get_public_resources(
            client=self.client,
            public_key=public_key,
            path=path
        )

        context = {
            'form': self.form_class(request.POST),
            'title': self.title,
            'public_resources_path': public_resources_path,
            'public_resources': public_resources,
            'public_key': public_key
        }

        return render(request, 'actions/public_link.html', context=context)


def clear_search(request):
    """ Функция для очистки полей формы поиска CityNameForm """

    redirect_url = reverse('actions:weather_forecast')
    return HttpResponseRedirect(redirect_url)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
