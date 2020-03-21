import os.path
from PIL import Image
import requests


def download_picture(url, path):
    res = requests.get(url, verify=False)
    res.raise_for_status()
    file = res.content
    path_to_file = os.path.split(path)[0]
    os.makedirs(path_to_file, exist_ok=True)
    with open(path, mode='wb') as infile:
        infile.write(file)


def get_file_exc(url):
    file = os.path.splitext(url)
    return file[1][1:]


def crop_photo(path, outfile='image/1112.jpg'):
    image = Image.open(f'{path}')
    if image.format != 'JPEG':
        image = image.convert('RGB')
    min_size = min(image.size)
    max_size = max(image.size)
    field = (max_size - min_size)//2
    image_size = (field, 0, min_size + field, min_size) if image.size[0] > image.size[1]\
        else (0, field, min_size, min_size + field)
    image = image.crop(image_size)
    image.save(outfile, format='JPEG')
    return outfile

