from requests_methods import BaseApi


class YandexDiskRestApi(BaseApi):
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url
        self.auth_header = {'Authorization': 'OAuth ' + self.token}

    def get_disk_metadata(self):
        r_metadata = self.get(url=self.url, headers=self.auth_header)
        return r_metadata

    def get_item_metadata(self, path: str):
        r_metadata = self.get(url=self.url + '/resources', headers=self.auth_header, params={'path': path})
        return r_metadata

    def make_dir(self, path: str = '/'):
        r_make_dir = self.put(url=self.url + '/resources', headers=self.auth_header, params={'path': path})
        return r_make_dir

    def delete_item(self, path: str):
        r_del_item = self.delete(url=self.url + '/resources', headers=self.auth_header, params={'path': path})
        return r_del_item

    def make_file(self, file: str, path: str = '/'):
        upload_link = self.get(url=self.url + '/resources/upload', headers=self.auth_header,
                               params={'path': path + file}).json()['href']
        r_upload_file = self.put(url=upload_link)
        return r_upload_file

    def restore_file_from_trash(self, file: str):
        r_restore_file = self.put(url=self.url + '/trash/resources/restore',
                                  headers=self.auth_header, params={'path': file})
        return r_restore_file

    def empty_trash(self):
        r_empty_trash = self.delete(url=self.url + '/trash/resources', headers=self.auth_header)
        return r_empty_trash
