from os import getenv
from dotenv import load_dotenv
from mugimugi import MugiMugi


load_dotenv()
client = MugiMugi(getenv("MUGIMUGI_API_KEY"))
