import requests

token = ''

def create_folder(path, token):
    headers = {'Accept': 'application/json',
    'Authorization': 'OAuth {}'.format(token)}
    params = {'path': path}
    url = 'https://cloud-api.yandex.net/put/v1/disk/resources'
    create_folder = requests.put(url, headers=headers, params=params)
    if create_folder.status_code == 201:
        print(f'Директория {path} создана')
    elif create_folder.status_code == 409:
        print(f'Директория {path} уже существует')
    else:
        print(f'Директория {path} не создана')
    return create_folder.status_code

if __name__ == '__main__':
    result = create_folder('My_folder1111', token)