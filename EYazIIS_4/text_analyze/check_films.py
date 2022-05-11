import random

video_url_list = []

def read_video_urls():
    global video_url_list
    with open('videos.txt') as f:
        video_url_list = f.readlines()


def get_video():
    read_video_urls()
    print(random.choice(video_url_list))
    return random.choice(video_url_list)



