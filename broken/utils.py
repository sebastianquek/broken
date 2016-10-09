import random
import re


def get_random_delay(min_time=0.01, max_time=0.1):
    """
    Random sleep time between min and max time. Defaults to between 10 and 100ms

    :param min_time: minimum time (s)
    :param max_time: maximum time (s)
    :return: time in seconds
    """
    return random.uniform(min_time, max_time)


def is_supported_content_type(raw_content_type):
    """
    Checks if the raw content type retrieved from the header is of
    the appropriate type for more links to be found from the given URL

    :param raw_content_type: raw content type header data
    :return:
    """
    if re.match(r'text/', raw_content_type):
        return True
    return False