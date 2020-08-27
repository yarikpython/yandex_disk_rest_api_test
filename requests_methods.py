import requests


class BaseApi:

    def get(self, url, headers=None, params=None):
        response = requests.get(url=url, headers=headers, params=params)
        return response

    def put(self, url, headers=None, params=None):
        response = requests.put(url=url, headers=headers, params=params)
        return response

    def delete(self, url, headers=None, params=None):
        response = requests.delete(url=url, headers=headers, params=params)
        return response
