def check_signup_headers(user_agent, udid):
    return {
        'authority': 'api1.vingle.net',
        'method': 'POST',
        'path': '/api/users',
        'scheme': 'https',
        'accept': 'application/vnd.vingle-v4+json',
        'accept-encoding': 'gzip, deflate, br',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.vingle.net',
        'referer': 'https://www.vingle.net/users/sign_up/username',
        'x-vingle-user-agent': 'Vingle Desktop Web/2020-05-07T11-05-16.723Z (Chrome/81.0.4044.138; Mac OS 10.14.6)',
        'x-vingle-udid': udid,
        'User-Agent': user_agent
    }


def check_confirm_account_headers(user_agent):
    return {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7',
        'Host': 'email.vingle.net',
        'Connection': 'keep-alive',
        'User-Agent': user_agent
    }


def check_validate_headers(user_agent, udid, validate, referer):
    return {
        'authority': 'api1.vingle.net',
        'method': 'GET',
        'path': validate,
        'scheme': 'https',
        'accept': 'application/vnd.vingle-v4+json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en',
        'origin': 'https://www.vingle.net',
        'referer': referer,
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'x-vingle-user-agent': 'Vingle Desktop Web/2020-05-07T11-05-16.723Z (Chrome/81.0.4044.138; Mac OS 10.14.6)',
        'x-vingle-udid': udid,
        'User-Agent': user_agent
    }
