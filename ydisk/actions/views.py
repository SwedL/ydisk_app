from datetime import date, timedelta

from django.core.cache import cache
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

# from common.views import WeatherSource

from .forms import LinkForm


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

        return render(request, 'actions/main.html', context=context)

    def post(self, request):
        error = None  # флаг указывающий ошибки получения данных по городу, для alert сообщения

        link = request.POST['link']
        print(link)

        context = {
            'form': self.form_class(request.POST),
            'title': self.title,
            'error': error,
        }

        return render(request, 'actions/main.html', context=context)


def clear_search(request):
    """ Функция для очистки полей формы поиска CityNameForm """

    redirect_url = reverse('actions:weather_forecast')
    return HttpResponseRedirect(redirect_url)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
