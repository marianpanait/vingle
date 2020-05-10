import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests.exceptions import ProxyError

from src.helpers.mailer import get_confirmation_mail
from src.helpers.request_data import check_signup_headers, check_validate_headers, check_confirm_account_headers
from src.helpers.utils import get_udid
from src.static.constants import REGISTER_URL, Response, VALIDATE_URL, SITE_MESSAGES


class Account:
    def __init__(self, email_object, proxy=None, user_agent=None):
        if not user_agent:
            ua = UserAgent()
            self.user_agent = ua.random
        else:
            self.user_agent = user_agent

        self.s = requests.Session()

        if proxy:
            self.s.proxies = {
                "http": proxy,
                "https": proxy,
                "ftp": proxy
            }
        else:
            self.s.proxies = {
                "http": None,
                "https": None,
                "ftp": None
            }

        self.email = email_object['email']
        self.password = email_object['password']
        self.username = email_object['username']
        self.confirmation_url = None

        self.udid = get_udid()
        self.is_logged_in = False

    def signup(self):
        try:

            user_data = "{\"email\":\"" + self.email + "\",\"password\":\"" + self.password + "\",\"username\":\"" + self.username + "\"}"
            print(f'{user_data} : {self.s.proxies["http"]} - signing up...')

            response = self.s.post(REGISTER_URL, headers=check_signup_headers(self.user_agent, udid=self.udid),
                                   data=user_data)

            soup = BeautifulSoup(response.content, features="lxml")

            response = json.loads(soup.text)

            if 'error' in response:
                print(f'Signup error {self.email}')
                print(response['error'])
                return False

            print(f'{self.email} - Signup success!')
            return True

        except ProxyError:
            print(f'SIGNUP ERROR: ProxyError {self.email}')
            return Response.PROXY_ERROR.value

        except Exception as e:
            print(f'SIGNUP Error: {self.email} {e}')
            return False

    def confirm_account(self):
        try:
            email_object = {'email': self.email, 'password': self.password}

            self.confirmation_url = get_confirmation_mail(email_object)

            if not self.confirmation_url:
                print(f'{self.email} confirmation mail not found; Exiting..')
                return False

            response = self.s.get(self.confirmation_url)
            soup = BeautifulSoup(response.content, features="lxml")

            if Response.ACCOUNT_CONFIRMED.value not in soup.prettify():
                print(f'Account confirmation failed - {self.email}')
                return False

            print(f'{self.email} - Account confirmed!')
            return True

        except ProxyError:
            print(f'Confirm Account ERROR: ProxyError {self.email}')
            return Response.PROXY_ERROR.value

        except Exception as e:
            print(f'Confirm account Error: {e}')
            return False
