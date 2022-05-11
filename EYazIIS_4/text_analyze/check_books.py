import random
import os

path_main = os.getcwd()
path_for_items = path_main + '/books/'


def find_books(message):
    if message.find('генетика') != -1:
        branch = "genetics"
        DIR = path_for_items+'/'+branch
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    elif message.find('общее') != -1:
        branch = "general"
        DIR = path_for_items+'/'+branch
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    elif message.find('анатомия') != -1:
        branch = "anathomy"
        DIR = path_for_items+'/'+branch
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    else:
        return open(path_main+'/error.jpg', 'rb')



