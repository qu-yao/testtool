import requests


class Request(object):

    def request_get(self, url, data):
        res = requests.post(url=url, data=data)
        res.encoding = "utf-8"
        return res.text

    def request_post(self, url, data):
        res = requests.post(url=url, data=data)
        res.encoding = "utf-8"
        return res.text
