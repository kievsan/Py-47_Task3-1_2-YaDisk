from pprint import pprint

import requests


def err_msg(http_code, msg=''):
    print(f'\n\tHttp code:\t{http_code}')
    err = int(http_code) / 100 >= 4
    if err:
        print(msg)
        print('Файл не загружен на Yandex.Disk!')
        print('Программа завершена')
    else:
        print("'Файл загружен на Yandex.Disk!'")
    return err


class YandexDisk:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Autorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        print(f'Запрашиваем Yandex.Disk API ссылку для загрузки файла {disk_file_path} ...')
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, params=params, headers=headers)
        if err_msg(response.status_code, 'Ссылка для загрузки файла не получена!'):
            quit(1)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        print(f'\nЗапишем файл {disk_file_path} на Yandex.Disk ...')
        href = self._get_upload_link(disk_file_path=disk_file_path)
        response = requests.put(href, data=open(filename, 'rb'))
        if err_msg(response.status_code):
            quit(1)
        response.raise_for_status()

