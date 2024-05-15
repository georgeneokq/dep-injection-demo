from urllib.request import urlopen
from json import loads

class HttpService:
    def get(self, url: str):
        response: bytes = urlopen(url).read()
        result: dict = loads(response.decode())
        return result