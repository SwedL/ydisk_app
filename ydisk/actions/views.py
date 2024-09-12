from datetime import date, timedelta

from django.core.cache import cache
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import LinkForm, UserLoginForm


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


class FollowLinkView(View):
    """ Представление главной страницы - получения публичной ссылки """

    title = 'Переход по ссылке'
    form_class = LinkForm

    # @property
    # def create_date(self):
    #     """ Функция создаёт и возвращает список дней недели"""
    #     dates_week = [date.today() + timedelta(days=i) for i in range(7)]
    #     return dates_week

    def get(self, request):
        # date_and_temperature_list = [{'date': d, 'temperature': '-'} for d in self.create_date]

        context = {
            'form': self.form_class,
            'title': self.title,
            # 'date_and_temperature_list': date_and_temperature_list,
        }

        return render(request, 'actions/public_link.html', context=context)

    def post(self, request):
        error = None  # флаг указывающий ошибки получения данных по городу, для alert сообщения

        link = request.POST['link']
        print(link)

        context = {
            'form': self.form_class(request.POST),
            'title': self.title,
            'error': error,
        }

        return render(request, 'actions/public_link.html', context=context)


def clear_search(request):
    """ Функция для очистки полей формы поиска CityNameForm """

    redirect_url = reverse('actions:weather_forecast')
    return HttpResponseRedirect(redirect_url)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
