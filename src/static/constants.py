import enum

REGISTER_URL = 'https://api1.vingle.net/api/users'
AUTHENTICATE_URL = 'https://api1.vingle.net/api/auth'
CREATE_POST_URL = 'https://api1.vingle.net/api/cards'
VALIDATE_URL = 'https://api1.vingle.net/api/users/validate?'


class Files(enum.Enum):
    POST_CONTENT = "src/static/post_content/article"
    POST_TITLE = "src/static/post_content/title"
    NICHES = "src/static/niches"
    CREATED_POSTS = "src/static/posts"


class Exceptions(enum.Enum):
    SIGNUP_ERROR = "Username or password missing"
    IP_BANNED = "IP is banned"


class SITE_MESSAGES(enum.Enum):
    SIGNUP_SUCCESS = "Your account was successfully confirmed. You can now sign in"
    ACCOUNT_CONFIRMED = 'You’re confirmed successfully'


class ProxyOption(enum.Enum):
    ROTATING = 'ROTATING'
    NO_PROXY = 'NO_PROXY'
    SINGLE_PROXY = 'SINGLE_PROXY'
    MULTIPLE_PROXIES = 'MULTIPLE_PROXIES'


class Response(enum.Enum):
    PROXY_ERROR = 'PROXY_ERROR'
    USERNAME_ERROR = 'Starting with alphabet'
