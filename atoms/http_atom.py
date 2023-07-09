import requests


class HttpAtom:
    def __init__(self, url, request_data):
        self.url = url
        self.request_data = request_data

    def http_post_request(self):
        response = requests.post(self.url,json=self.request_data)
        return response.json()


