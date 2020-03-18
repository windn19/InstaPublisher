import requests
from prepare_file import download_picture, get_file_exc


def fetch_spacex_last_launch():
    res = requests.get('https://api.spacexdata.com/v3/launches/latest')
    res.raise_for_status()
    data = res.json()
    images = data['links']['flickr_images']
    for num, image in enumerate(images[:1]):
        download_picture(url=image, path=f'image/spaceX{(num + 1)}.{get_file_exc(image)}')
        print(f'File {image}')
