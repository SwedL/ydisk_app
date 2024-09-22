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

# @shared_task()
# def download_select_resources(download_resources):
#     client = yadisk.AsyncClient()
#
#     async def main():
#         async with client:
#             tasks = [client.download_public(dr[0], dr[1], path=dr[2]) for dr in download_resources]
#
#             await asyncio.gather(*tasks)
#     asyncio.run(main())

# views.py
#     def download_files(self, public_key: str, path: str, selected_resources: list):
#         """Функция скачивания выбранных файлов"""
#         download_resources = []
#
#         with self.client:
#             public_resources, public_resources_path = self.get_public_resources(public_key=public_key, path=path)
#             download_public_resources = [pr for pr in public_resources if pr.name in selected_resources]
#             for dpr in download_public_resources:
#                 if dpr.type == 'dir':
#                     download_folder = str(os.path.join(Path.home(), f"Downloads\\{dpr.name}.zip"))
#                 else:
#                     download_folder = str(os.path.join(Path.home(), f"Downloads\\{dpr.name}"))
#
#                 download_path = dpr.path.replace('*', '/')
#                 download_resources.append((public_key, download_folder, download_path))
#                 print(public_key, download_folder, download_path, sep="\n")
#
#         download_select_resources.delay(download_resources)


