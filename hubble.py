import requests
from prepare_file import download_picture, get_file_exc


def fetch_hubble_image():
    url = "http://hubblesite.org//api/v3/images/wallpaper"
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    for idi in data[:1]:
        idi = idi['id']
        url = f'http://hubblesite.org//api/v3/image/{idi}/'
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()['image_files']
        url_file = 'http:' + data[-1]['file_url']
        download_picture(url_file, path=f'image/hubble{idi}_{len(data) - 1}.{get_file_exc(url_file)}')
        print(f'File loaded {url}')
