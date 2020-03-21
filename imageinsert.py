import urllib3
import instabot
from dotenv import load_dotenv
from hubble import fetch_hubble_image
from space import fetch_spacex_last_launch
from prepare_file import crop_photo
from os import listdir, remove, getenv


def main():
    load_dotenv()
    login = getenv('INSTAGRAM_LOGIN')
    password = getenv('INSTAGRAM_PASSWORD')
    bot = instabot.Bot()
    bot.login(username=login, password=password)
    urllib3.disable_warnings()
    fetch_spacex_last_launch()
    fetch_hubble_image()
    for name in listdir('image'):
        file = crop_photo(f'image/{name}')
        bot.upload_photo(file)
        remove(f'{file}.REMOVE_ME')


if __name__ == '__main__':
    main()
