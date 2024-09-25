import os
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from yadisk import Client
from actions.tasks import download_select_resources


@dataclass
class PublicResource:
    name: str
    type: str
    path: str
    download_link: str


class YandexClient:
    client = Client()

    def get_public_resources(self, public_key: str, path: str) -> Tuple:
        """
        Функция получает все публичные ресурсы по заданному пути,
        возвращает кортеж из списка публичных ресурсов и путь,
        для отображение в строке интерфейса пользователя
        """

        if '*' in path:
            path = path.replace('*', '/')

        with self.client:
            raw_data_public_resources = self.client.get_public_meta(public_key, path=path)
            public_resources = []

            for s in raw_data_public_resources.public_listdir(path=path):
                public_resources.append(PublicResource(
                    name=s['name'],
                    type=s['type'],
                    path=s['path'].replace('/', '*'),
                    download_link=s['file'],
                ))

        return public_resources, raw_data_public_resources.path

    def download_files(self, public_key: str, path: str, selected_resources: list):
        """Функция скачивания выбранных файлов"""

        with self.client:
            public_resources, public_resources_path = self.get_public_resources(public_key=public_key, path=path)
            download_public_resources = [pr for pr in public_resources if pr.name in selected_resources]
            for dpr in download_public_resources:
                if dpr.type == 'dir':
                    download_folder = str(os.path.join(Path.home(), f"Downloads\\{dpr.name}.zip"))
                else:
                    print(str(os.path.join(Path.home(), "")))
                    download_folder = str("".join(["/ydisk", f"/{dpr.name}"]))
                    print(download_folder)
                download_path = dpr.path.replace('*', '/')
                download_select_resources.delay(public_key, download_folder, download_path)

    def download_all(self, public_key: str, path: str):
        """Функция скачивания всей текущей директории одним архивом"""

        with self.client:
            if len(path) == 1:
                # верхний уровень, получаем имя публичного ресурса
                public_resources_name = self.client.get_public_meta(public_key).name
                public_resources_path = '/'
            else:
                # иначе имя берём из пути
                public_resources, public_resources_path = self.get_public_resources(
                    public_key=public_key,
                    path=path,
                )
                public_resources_name = public_resources_path.rpartition('/')[-1]

            download_folder = str(os.path.join(Path.home(), f"Downloads\\{public_resources_name}.zip"))
            download_select_resources(public_key, download_folder, path=public_resources_path)
