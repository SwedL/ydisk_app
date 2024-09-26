import yadisk
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.cache import cache
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from common.views import YandexClient

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


class PublicKeyView(View, YandexClient):
    """ Представление страницы получения публичной ссылки """

    title = 'Публичная ссылка'
    form_class = LinkForm

    def get(self, request, public_key: str = None, path: str = None):
        context = {
            'form': self.form_class(),
            'title': self.title,
        }

        if path:
            data_from_cache = cache.get('/'.join([public_key, path]))
            if data_from_cache:
                public_resources, public_resources_path = data_from_cache
            else:
                try:
                    public_resources, public_resources_path = self.get_public_resources(
                        public_key=public_key,
                        path=path
                    )
                    cache.set('/'.join([public_key, path]), (public_resources, public_resources_path), 3600)
                except yadisk.exceptions.NotFoundError:
                    return redirect(reverse('actions:public_key'))

            context.update({
                'form': self.form_class({'public_key': public_key}),
                'public_resources_path': public_resources_path,
                'public_resources': public_resources,
                'public_key': public_key
            })

        return render(request, 'actions/public_key.html', context=context)

    def post(self, request, public_key: str = None, path: str = '/'):
        public_key = request.POST.get('public_key')

        if request.POST.get('enter_public_key'):
            reverse_url = reverse('actions:public_key', kwargs={'public_key': public_key, 'path': '*'})
            return redirect(reverse_url)

        if request.POST.get('level_up'):
            pre_path = path.rpartition('*')[0]  # при перемещении на уровень вверх убираем заднюю часть из пути
            path = pre_path if pre_path else '*'  # если верхн. уровень, то '*', заменится на '/' в get_public_resources
            reverse_url = reverse('actions:public_key', kwargs={'public_key': public_key, 'path': path})
            return redirect(reverse_url)

        if request.POST.get('download_selected'):
            selected_resources = [v for k, v in request.POST.items() if k.isdigit()]
            self.download_files(public_key=public_key, path=path, selected_resources=selected_resources)

        if request.POST.get('download_all'):
            self.download_all(public_key=public_key, path=path)

        public_resources, public_resources_path = self.get_public_resources(public_key=public_key, path=path)

        context = {
            'form': self.form_class(request.POST),
            'title': self.title,
            'public_resources_path': public_resources_path,
            'public_resources': public_resources,
            'public_key': public_key
        }

        return render(request, 'actions/public_key.html', context=context)


def clear_link(request):
    """ Функция очистки поля формы публичной ссылки """
    redirect_url = reverse('actions:public_key')
    return redirect(redirect_url)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def logout_user(request):
    logout(request)
    return redirect('/')
