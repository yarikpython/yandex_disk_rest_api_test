import pytest
from yandex_disk_rest_api import YandexDiskRestApi
from config import YANDEX_API_TOKEN, YANDEX_DISK_URL


@pytest.fixture()
def yandex_disk():
    yandex_disk = YandexDiskRestApi(token=YANDEX_API_TOKEN, url=YANDEX_DISK_URL)
    yield yandex_disk
    yandex_disk.empty_trash()

