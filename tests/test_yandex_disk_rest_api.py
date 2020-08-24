import allure


@allure.feature('Directories and files')
@allure.story('Создание и удаление директории')
def test_make_and_del_dir(yandex_disk):
    yandex_disk.make_dir(path='/test_dir')
    yandex_disk.delete_item(path='/test_dir')
    assert yandex_disk.get_item_metadata(path='/test_dir').status_code == 404


@allure.feature('Directories and files')
@allure.story('Создание и удаление директории и файла')
def test_make_and_del_file(yandex_disk):
    yandex_disk.make_dir(path='/test_dir')
    yandex_disk.make_file(path='/test_dir/', file='file.txt')
    yandex_disk.delete_item(path='/test_dir/file.txt')
    yandex_disk.delete_item(path='/test_dir')
    assert yandex_disk.get_item_metadata(
        path='/test_dir/file.txt').status_code == 404 and yandex_disk.get_item_metadata(
        path='/test_dir').status_code == 404


@allure.feature('Trash')
@allure.story('Восстановление из корзины')
def test_restore_file(yandex_disk):
    yandex_disk.make_dir(path='/test_dir')
    yandex_disk.make_file(path='/test_dir/', file='file.txt')
    yandex_disk.delete_item(path='/test_dir/file.txt')
    yandex_disk.restore_file_from_trash(file='file.txt')
    assert yandex_disk.get_item_metadata('/test_dir/file.txt').status_code == 200
    yandex_disk.delete_item(path='/test_dir')


@allure.feature('Trash')
@allure.story('Проверка размера корзины')
def test_trash_size(yandex_disk):
    trash_size = yandex_disk.get_disk_metadata().json()['trash_size']
    yandex_disk.make_dir(path='/test_dir')
    yandex_disk.make_file(path='/test_dir/', file='file.txt')
    yandex_disk.make_file(path='/test_dir/', file='file_2.txt')
    yandex_disk.delete_item(path='/test_dir/file.txt')
    yandex_disk.delete_item(path='/test_dir/file_2.txt')
    new_trash_size = yandex_disk.get_disk_metadata().json()['trash_size']
    assert new_trash_size == trash_size + new_trash_size
    yandex_disk.restore_file_from_trash(file='file.txt')
    yandex_disk.delete_item(path='/test_dir')


@allure.feature('Trash')
@allure.story('Создание директорий и файлов, удаление их в корзину')
def test_expexted_params(yandex_disk):
    yandex_disk.make_dir(path='/test_dir')
    yandex_disk.make_dir(path='/test_dir/foo')
    yandex_disk.make_file(path='/test_dir/foo/', file='autotest.txt')
    assert 'foo' == yandex_disk.get_item_metadata(path='/test_dir').json()['_embedded']['items'][0]['name']
    yandex_disk.delete_item(path='/test_dir/foo/autotest.txt')
    yandex_disk.delete_item(path='/test_dir/foo')
    yandex_disk.delete_item(path='/test_dir')
    assert yandex_disk.get_item_metadata(path='/test_dir').status_code == 404
    assert yandex_disk.get_item_metadata(path='/test_dir/foo').status_code == 404
    assert yandex_disk.get_item_metadata(path='/test_dir/foo/autotest.txt').status_code == 404


@allure.feature('Trash')
@allure.story('Очистка корзины')
def test_empty_trash(yandex_disk):
    yandex_disk.make_dir(path='/test_dir')
    yandex_disk.make_dir(path='/test_dir/foo')
    yandex_disk.make_file(path='/test_dir/foo/', file='autotest.txt')
    yandex_disk.delete_item(path='/test_dir')
    yandex_disk.empty_trash()
    assert yandex_disk.get_disk_metadata().json()['trash_size'] == 0
