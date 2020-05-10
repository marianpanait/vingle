import json
import random
import re

from spinning import spinning

from src.Account import Account
from src.actions.utils import retry_while_proxy_error
from src.config import proxy_value
from src.helpers.file_manager import FileManager
from src.helpers.utils import get_shortened_content, get_niche, get_game_name_from_hackerone_url, get_first_name, \
    get_last_name
from src.static.constants import Response, Files

file_manager = FileManager()


def create_account(acc, profile_data):
    profile_data = profile_data
    profile_data['username'] = f'{get_first_name()}{get_last_name()}hack'
    acc.username = profile_data['username']

    signup_respone = retry_while_proxy_error(acc.signup)

    if signup_respone is not True and signup_respone is Response.USERNAME_ERROR.value:
        create_account(acc, profile_data)
        return

    if not signup_respone:
        return

    auth_response = retry_while_proxy_error(acc.authenticate_user)

    if not auth_response:
        return

    confirmation_response = retry_while_proxy_error(acc.confirm_account)

    if not confirmation_response:
        return

    create_article_response = retry_while_proxy_error(acc.create_article, profile_data)

    if not create_article_response:
        return

    return True


def create_vg_account():
    line = file_manager.get_first_line(file=Files.NICHES.value)

    niche = get_niche(line)
    hack_url = niche['url']

    game_name = get_game_name_from_hackerone_url(hack_url)
    username = 'nebagampulanvingle'

    email_obj = {'email': niche['email'], 'password': niche['password'], 'username': username}
    print(f'game: {game_name}')

    acc = Account(email_object=email_obj, proxy=None)

    article_no = random.randint(1, 3)

    with open(f'{Files.POST_CONTENT.value}{article_no}', 'r') as f:
        post_content = f.read()

    with open(Files.POST_TITLE.value) as f:
        title_components = json.load(f)

    post_title = get_post_title(title_components, game_name)
    post_title = get_shortened_content(post_title, 99) if len(post_title) > 99 else post_title

    post_content = spinning.unique(post_content)
    post_content = post_content.replace("_GAME_", game_name)
    post_content = post_content.replace("_HACK_", hack_url)

    article_data = {
        'title': post_title,
        'content': post_content
    }

    create_account(acc, article_data)
    data = f'{acc.email} | {acc.password} | {game_name} | {acc.post_url}\n'

    if acc.post_url:
        file_manager.append_to_file(file=Files.CREATED_POSTS.value, data=data)
        file_manager.remove_line(file=Files.NICHES.value, data=hack_url)


def get_post_title(title_components, game_name):
    title_first_part = spinning.unique(title_components['title_part1']).replace("_GAME_", game_name)
    title_second_part = spinning.unique(title_components['title_part2']).replace("_GAME_", game_name)
    title_third_part = spinning.unique(title_components['title_part3']).replace("_GAME_", game_name)

    titles = [title_first_part, title_second_part, title_third_part]

    post_title = random.choice(titles)

    return post_title
