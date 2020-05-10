import random
import time

from requests.exceptions import ProxyError

from src.static.constants import Files


def set_timeout(timeout_range):
    time.sleep(random.randint(timeout_range[0], timeout_range[1]))


def retry_while_proxy_error(f, *args):
    try:
        resp = f(*args)
        return resp
    except ProxyError as e:
        print(e)
        time.sleep(1)
        f(*args)
    except Exception as e:
        print(f'Failed {e}')