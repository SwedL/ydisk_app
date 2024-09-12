from dataclasses import dataclass


@dataclass
class PublicResource:
    name: str
    type: str
    path: str
    download_link: str
