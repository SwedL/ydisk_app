from dataclasses import dataclass
from typing import Tuple
from yadisk import Client


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

