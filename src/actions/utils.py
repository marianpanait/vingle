import random
import time


def set_timeout(timeout_range):
    time.sleep(random.randint(timeout_range[0], timeout_range[1]))