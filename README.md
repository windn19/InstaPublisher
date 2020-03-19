# Space Instagram

 The program downloads photos of the last launch of spaceX and photos from the Wallpaper Hubble collection, and uploads them to an existing Instagram account

### How to install

Python3 should already be installed.
Then use `pip` (or` pip3`, there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```
At the root of the project, an .env file must exist with the following information:
```
INSTAGRAM_LOGIN = '[your Instagram login]'
INSTAGRAM_PASSWORD = '[your password for Instagram login]'
```

### Objective of the project

The code is written for educational purposes on the online course for web developers [dvmn.org] (https://dvmn.org/).
