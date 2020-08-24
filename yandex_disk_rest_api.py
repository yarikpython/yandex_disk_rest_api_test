import requests


class YandexDiskRestApi:
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url

    def get_disk_metadata(self):
        r_metadata = requests.get(url=self.url, headers={'Authorization': 'OAuth ' + self.token})
        return r_metadata

    def get_item_metadata(self, path: str):
        r_metadata = requests.get(url=self.url + '/resources', headers={'Authorization': 'OAuth ' + self.token},
                                  params={'path': path})
        return r_metadata

    def make_dir(self, path: str = '/'):
        r_make_dir = requests.put(url=self.url + '/resources', headers={'Authorization': 'OAuth ' + self.token},
                                  params={'path': path})
        return r_make_dir

    def delete_item(self, path: str):
        r_del_item = requests.delete(url=self.url + '/resources', headers={'Authorization': 'OAuth ' + self.token},
                                     params={'path': path})
        return r_del_item

    def make_file(self, file: str, path: str = '/'):
        upload_link = requests.get(url=self.url + '/resources/upload', headers={'Authorization': 'OAuth ' + self.token},
                                   params={'path': path + file}).json()['href']
        r_upload_file = requests.put(url=upload_link)
        return r_upload_file

    def restore_file_from_trash(self, file: str):
        r_restore_file = requests.put(url=self.url + '/trash/resources/restore',
                                      headers={'Authorization': 'OAuth ' + self.token}, params={'path': file})
        return r_restore_file

    def empty_trash(self):
        r_empty_trash = requests.delete(url=self.url + '/trash/resources',
                                        headers={'Authorization': 'OAuth ' + self.token})
        return r_empty_trash
