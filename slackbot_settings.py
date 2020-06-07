import os

from dotenv import load_dotenv


load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
DEFAULT_REPLY = "どうでもいいけど、アルクアラウンド聞いて？"
ERROR_TO = os.getenv('ERROR_TO')

PLUGINS = [
    'plugins',
]
