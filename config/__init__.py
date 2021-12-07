from .mysql import *
from dotenv import find_dotenv, load_dotenv


ENV_FILE = find_dotenv(filename='.env')

if ENV_FILE:
    load_dotenv(ENV_FILE)
else:
    raise FileNotFoundError(ENV_FILE)
