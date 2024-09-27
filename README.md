<p align="center"><img src="https://i.ibb.co/vJnDKGB/picture-compress.png" alt="Main-logo" border="0" width="500"></p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.11-orange)" alt="Aiogram Version">
   <img src="https://img.shields.io/badge/Django-5.1.1-E86F00" alt="Aiohttp Version">
</p>

<p>WEB - приложение предоставляет возможность взаимодействия с API Яндекс.Диска.
<br>Просмотр и скачивание файлов с Яндекс.Диска по публичной ссылке.</p>


## Описание работы
После того как пользователь проходит процесс авторизации.
Открывается страница работы с публичной ссылкой.<br>
В поле вводим публичную ссылку, нажимаем кнопку Enter. В интерфейсе отобразится список файлов и папок публичной ссылки.<br>
Кнопка "X" очищает поле ввода.

При успешном открытии публичной ссылки, появится окно вложенности папок,
кнопка возврата на верхний уровень, а также кнопка скачивания выбранных
файлов и кнопка скачивания всей папки одним архивом .zip.<br>
Файлы, папки и архивы скачиваются в папку приложения "downloads".

Списки файлов кэшируются, для обеспечения быстродействия приложения.

<p align="center">
<a href="https://i.ibb.co/ZTXLtb3/login-page.png"><img src="https://i.ibb.co/ZTXLtb3/login-page.png" alt="2024-03-08-14-02-52" border="0"></a>
</p>
<p align="center">
<a href="https://i.ibb.co/sygSRRY/public-key-page3.png"><img src="https://i.ibb.co/sygSRRY/public-key-page3.png" alt="2024-03-08-14-02-52" border="0"></a>
</p>
<p align="center">
<a href="https://i.ibb.co/mDz1wyZ/public-key-page1.png"><img src="https://i.ibb.co/mDz1wyZ/public-key-page1.png" alt="2024-03-08-14-02-52" border="0"></a>
</p>
<p align="center">
<a href="https://i.ibb.co/xzHp4HM/public-key-page2.png"><img src="https://i.ibb.co/xzHp4HM/public-key-page2.png" alt="2024-03-08-14-02-52" border="0"></a>
</p>


## Установка

Скачайте код:
```sh
git clone https://github.com/SwedL/ydisk_app.git
```
Перейдите в каталог проекта `ydisk_app`.<br>
```sh
cd ydisk_app
```
Создайте файл `.env` с переменными окружения и положите туда такой код:<br>

```sh
DEBUG=True
REDIS_URL=redis://redis:6379
SECRET_KEY='vu1c-=svhigsn81!1doknfa2zxchlq&^37vdyqgc165a8wswjr'
```
! **Важно**: SECRET_KEY замените на свой.<br>

Создайте виртуальное окружение:
- Windows: `python -m venv venv`
- Linux: `python3 -m venv venv`

Активируйте его командой:
- Windows: `.\venv\Scripts\activate`
- Linux: `source venv/bin/activate`

Перейдите в каталог приложения `ydisk`.<br>
```sh
cd ydisk
```
Установите зависимости в виртуальное окружение:

```sh
pip install -r requirements.txt
```

Для обеспечения выполнения фоновых асинхронных задач, в качестве брокера сообщений, необходимо установить и запустить Redis.  
https://redis.io/docs/install/install-redis/

Создайте необходимые таблицы базы данных командой:
```sh
python manage.py migrate
```
Создайте модель суперпользователя командой:
```sh
python manage.py createsuperuser
```
Запустите worker Celery:
```sh
- Windows: `celery -A ydisk worker -P eventlet --loglevel=info`
- Linux: `celery -A ydisk worker`
```

Откройте новое окно терминала, снова активируйте виртуальное окружение командой:
- Windows: `.\venv\Scripts\activate`
- Linux: `source venv/bin/activate`

Перейдите в каталог приложения `ydisk`.<br>
```sh
cd ydisk
```

Запустите сервер:
```sh
python manage.py runserver
```
Сервер работает на адресе <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>

## Как запустить приложение в Docker.
Скачайте код:
```sh
git clone https://github.com/SwedL/ydisk_app.git
```
Перейдите в каталог проекта `ydisk_app`.<br>
```sh
cd ydisk_app
```
Создайте файл `.env` с переменными окружения и положите туда такой код:<br>

```sh
DEBUG=True
REDIS_URL=redis://redis:6379
SECRET_KEY='vu1c-=svhigsn81!1doknfa2zxchlq&^37vdyqgc165a8wswjr'
```
! **Важно**: SECRET_KEY замените на свой.<br>

Выполните сборку образа:
```sh
docker-compose build
```
Запустите контейнер:
```sh
docker-compose up -d
```
Создайте суперпользователя:
```sh
docker exec -it ydisk python manage.py createsuperuser
```
Сервер работает на адресе <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>

### Тестирование

Проект покрыт тестами моделей, форм, представлений и url.<br>
Тесты запускаются командой:
```sh
python manage.py test
```
В docker:
```sh
docker exec -it ydisk python manage.py test
```
## Автор проекта

* **Осминин Алексей** - [SwedL](https://github.com/SwedL)

