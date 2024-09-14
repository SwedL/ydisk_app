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
from common.views import PublicResource


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

    def get(self, request):
        context = {
            'form': self.form_class,
            'title': self.title,
        }

        return render(request, 'actions/public_link.html', context=context)

    def post(self, request):
        public_key = request.POST['public_key']
        raw_data_public_resources = self.client.get_public_meta(public_key)

        public_resources = []
        for s in raw_data_public_resources.public_listdir():
            public_resources.append(PublicResource(
                name=s['name'],
                type=s['type'],
                path=s['path'],
                download_link=s['file']
            ))

        print(public_resources)

        context = {
            'form': self.form_class(request.POST),
            'title': self.title,
        }

        return render(request, 'actions/public_link.html', context=context)


def clear_search(request):
    """ Функция для очистки полей формы поиска CityNameForm """

    redirect_url = reverse('actions:weather_forecast')
    return HttpResponseRedirect(redirect_url)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
