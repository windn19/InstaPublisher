import os.path
from PIL import Image
import requests


def download_picture(url, path):
    res = requests.get(url, verify=False)
    res.raise_for_status()
    file = res.content
    dir = os.path.split(path)[0]
    os.makedirs(dir, exist_ok=True)
    with open(path, mode='wb') as infile:
        infile.write(file)


def get_file_exc(url):
    file = os.path.split(url)
    return file[1][-3:]


def instaphoto(path):
    image = Image.open(f'{path}')
    if image.format != 'JPEG':
        image = image.convert('RGB')
    m = min(image.size)
    mm = max(image.size)
    first_s = (mm - m)//2
    image_size = (first_s, 0, m + first_s, m)
    image = image.crop(image_size)
    fmt = get_file_exc(path)
    image.save(f'image/1112.jpg', format='JPEG')

