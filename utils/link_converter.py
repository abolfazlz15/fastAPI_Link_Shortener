from python_random_strings import random_strings

from database import collection_name


def generate_short_link():

    random_flag = random_strings.random_letters(10)
    return random_flag


def create_short_link_record(link_address: str) -> str:

    random_link = generate_short_link()

    collection_name.insert_one({'link': link_address, 'short_link': random_link})

    return random_link