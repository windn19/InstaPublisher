import requests
from prepare_file import download_picture, get_file_exc


def fetch_hubble_image():
    url = "http://hubblesite.org//api/v3/images/wallpaper"
    res = requests.get(url)
    res.raise_for_status()
    images = res.json()
    for image in images:
        id_image = image['id']
        url = f'http://hubblesite.org//api/v3/image/{id_image}/'
        res = requests.get(url)
        res.raise_for_status()
        id_images = res.json()['image_files']
        url_file = 'http:' + id_images[-1]['file_url']
        download_picture(url_file, path=f'image/hubble{id_image}_{len(id_images) - 1}.{get_file_exc(url_file)}')

