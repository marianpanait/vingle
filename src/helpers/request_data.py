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


def check_auth_headers(user_agent, udid):
    return {
        'authority': 'api1.vingle.net',
        'accept-language': 'en',
        'accept': 'application/vnd.vingle-v4+json',
        'x-vingle-user-agent': 'Vingle Desktop Web/2020-05-07T11-05-16.723Z (Chrome/81.0.4044.138; Mac OS 10.14.6)',
        'x-vingle-udid': udid,
        'user-agent': user_agent,
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.vingle.net',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.vingle.net/users/sign_up/username'
    }


def check_confirm_account_headers(user_agent):
    return {
        'User-Agent': user_agent
    }


def check_create_article_headers(user_agent, udid, auth_token):
    return {
        'authority': 'api1.vingle.net',
        'accept-language': 'en',
        'accept': 'application/vnd.vingle-v4+json',
        'x-vingle-authentication-token': auth_token,
        'x-vingle-user-agent': 'Vingle Desktop Web/2020-05-07T11-05-16.723Z (Chrome/81.0.4044.138; Mac OS 10.14.6)',
        'x-vingle-udid': udid,
        'user-agent': user_agent,
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.vingle.net',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.vingle.net/writing_form/new'
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
