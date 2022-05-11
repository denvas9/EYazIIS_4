import random

website_url_list = []

def read_website_urls():
    global website_url_list
    with open('websites.txt') as f:
        website_url_list = f.readlines()



def get_site():
    read_website_urls()
    print(random.choice(website_url_list))
    return random.choice(website_url_list)



