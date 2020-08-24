import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

YANDEX_API_TOKEN = os.environ.get('YANDEX_OAUTH_TOKEN')
YANDEX_DISK_URL = 'https://cloud-api.yandex.net/v1/disk'