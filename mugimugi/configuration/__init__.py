from os import getenv
from urllib.parse import urljoin
from dotenv import load_dotenv

load_dotenv()

HOST_NAME = "https://www.doujinshi.org/"
API_KEY = getenv("MUGIMUGI_API_KEY")
API_PATH = "api/"

# 404 if no final "/"
API = urljoin(urljoin(HOST_NAME, API_PATH), API_KEY) + "/"
