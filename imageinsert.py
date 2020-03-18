import urllib3
import instabot
from hubble import fetch_hubble_image
from space import fetch_spacex_last_launch
from prepare_file import instaphoto
from os import listdir, remove


if __name__ == '__main__':
    bot = instabot.Bot()
    bot.login(username="noscoff20", password="rjydthn")
    urllib3.disable_warnings()
    fetch_spacex_last_launch()
    fetch_hubble_image()
    for name in listdir('image'):
        instaphoto(f'image/{name}')
        bot.upload_photo('image/1112.jpg')
    remove('image/1112.jpg.REMOVE_ME')


