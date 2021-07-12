from mugimugi_client_api import MugiMugiClient
from mugimugi_client_image import MugiMugiImageClient


class API:
    IMAGE_API = MugiMugiImageClient()

    data: MugiMugiClient
    image: MugiMugiImageClient = IMAGE_API
    # web

    def __init__(self, key: str) -> None:
        self.data = MugiMugiClient(key)
