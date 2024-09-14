from dataclasses import dataclass
import yadisk


@dataclass
class PublicResource:
    name: str
    type: str
    path: str
    download_link: str


def get_public_resources(client, public_key, path):
    with client:
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

