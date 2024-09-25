from celery import shared_task
import pycurl
import yadisk


@shared_task()
def download_select_resources(public_key, download_folder, path):
    with yadisk.Client(session="pycurl") as client:
        client.download_public(public_key, download_folder, path=path, n_retries=2, curl_options={
            pycurl.MAX_SEND_SPEED_LARGE: 5 * 1024 ** 2,
            pycurl.MAX_RECV_SPEED_LARGE: 5 * 1024 ** 2,
            pycurl.MAXREDIRS: 15
        }
                           )
# celery -A ydisk flower

# celery -A ydisk worker -P eventlet --loglevel=info
