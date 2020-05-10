import re
import uuid

import faker
from faker import Faker

faker = Faker()


def get_udid():
    return str(uuid.uuid1())


def get_shortened_content(content, size):
    while len(content) > size:
        content = ' '.join(content.split(' ')[:-1])

    return content


def get_niche(line):
    line = line.split("|")

    niche = {'email': line[0],
             'password': line[1],
             'url': line[2]}

    return niche


def get_game_name_from_hackerone_url(hack_url):
    if '_hack' in hack_url:
        game_name = re.search('https://hackerone\.com/(.*?)_hack', hack_url).group(1)
    else:
        game_name = hack_url.split('.com')[1]
        game_name = game_name.replace('/', '')

    game_name = game_name.replace("_", " ")

    return game_name


def get_first_name():
    return faker.first_name()


def get_last_name():
    return faker.last_name()
