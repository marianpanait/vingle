from src.Account import Account
from src.config import proxy_value
from src.helpers.mailer import get_confirmation_mail
from src.static.constants import Response

email_object = {'username': 'reythooooolaw', 'email': 'RosenzweigRayia1998@bk.ru', 'password': 'Dqrgsy8jJE'}
acc = Account(email_object=email_object, proxy=None)
# r = acc.signup()
#
# if r != False and r is not Response.PROXY_ERROR.value:
acc.confirm_account()