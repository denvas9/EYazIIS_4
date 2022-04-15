import random
import os

path = os.getcwd() + '/books/'


def find_books(message):
    if message.find('приключения') != -1 or message.find('приключение') != -1:
        genre = "adventures"
        DIR = path+'/'+genre
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    elif message.find('комиксы') != -1 or message.find('комикс') != -1:
        genre = "comics"
        DIR = path+'/'+genre
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    elif message.find('фантастика') != -1:
        genre = "fantasy"
        DIR = path+'/'+genre
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    elif message.find('ужас') != -1 or message.find('ужасы') != -1:
        genre = "horrors"
        DIR = path+'/'+genre
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    elif message.find('роман') != -1 or message.find('романы') != -1:
        genre = "novels"
        DIR = path+'/'+genre
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    elif message.find('поэзия') != -1 or message.find('поэзии') != -1:
        genre = "poetry"
        DIR = path+'/'+genre
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    elif message.find('детективы') != -1 or message.find('детектив') != -1:
        genre = "detectives"
        DIR = path+'/'+genre
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    elif message.find('психология') != -1:
        genre = "psychology"
        DIR = path+'/'+genre
        return open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    else:
        return open(path+'error.jpg', 'rb')



