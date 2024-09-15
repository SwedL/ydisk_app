import os
from dataclasses import dataclass
from typing import Tuple
from yadisk import Client
from pathlib import Path



@dataclass
class PublicResource:
    name: str
    type: str
    path: str
    download_link: str


def get_public_resources(client: Client, public_key: str, path: str) -> Tuple:
    with client:
        if '*' in path:
            path = path.replace('*', '/')
        raw_data_public_resources = client.get_public_meta(public_key, path=path)

    public_resources_path = raw_data_public_resources.path
    public_resources = []
    for s in raw_data_public_resources.public_listdir(path=path):
        public_resources.append(PublicResource(
            name=s['name'],
            type=s['type'],
            path=s['path'].replace('/', '*'),
            download_link=s['file']
        ))

    return public_resources, public_resources_path


def download_files(client: Client, public_key: str, path: str, selected_resources: list):
    with client:
        public_resources, public_resources_path = get_public_resources(client=client, public_key=public_key, path=path)
        download_public_resources = [df for df in public_resources if df.name in selected_resources]
        for dpr in download_public_resources:
            if dpr.type == 'dir':
                download_folder = str(os.path.join(Path.home(), f"Downloads\\{dpr.name}.zip"))
            else:
                download_folder = str(os.path.join(Path.home(), f"Downloads\\{dpr.name}"))
            download_path = dpr.path.replace('*', '/')
            client.download_public(public_key, download_folder, path=download_path)


