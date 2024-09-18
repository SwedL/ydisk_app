import yadisk
import os
from dotenv import load_dotenv
from celery import shared_task, group
import pycurl


@shared_task()
def download_select_resources(public_key, download_folder, path):
    with yadisk.Client(session="pycurl") as client:
        client.download_public(public_key, download_folder, path=path, n_retries=1,
                               curl_options={
                                   pycurl.MAX_SEND_SPEED_LARGE: 5 * 1024 ** 2,
                                   pycurl.MAX_RECV_SPEED_LARGE: 5 * 1024 ** 2,
                                   # pycurl.PROXY: "http://localhost:8000",
                                   pycurl.MAXREDIRS: 15
                               }
                               )
    print(f'Файл скачан')

# celery -A ydisk worker -P eventlet --loglevel=info
