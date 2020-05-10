import quopri
import re
import sys
import imaplib
import email
import email.header
import itertools

from bs4 import BeautifulSoup

from src.actions.utils import set_timeout
from urlextract import URLExtract

EMAIL_FOLDER = "INBOX"


def process_mailbox(mailbox):
    url = None
    rv, data = mailbox.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in itertools.islice(reversed(data[0].split()), 5):
        rv, data = mailbox.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        if 'notifications@vingle.net' in msg['From'] and 'Confirm your Vingle account' in msg['Subject']:
            message_content = str(msg.get_payload())
            message_content = quopri.decodestring(message_content, header=False)

            soup = BeautifulSoup(message_content, 'html.parser')
            url = soup.select('a[class="main-action-btn"]')[0]['href']

            break

    return url


def get_confirmation_mail(user_details):
    url = None
    print(f'{user_details} is waiting for confirmation mail')
    print("Be patient..it will take a while")

    for i in range(1, 20):
        set_timeout([10, 11])
        email_address = user_details['email']
        password = user_details['password']

        try:
            mailbox = imaplib.IMAP4_SSL('imap.mail.ru')
        except Exception as e:
            print(e)
            continue

        try:
            rv, data = mailbox.login(email_address, password)
        except imaplib.IMAP4.error:
            print("GET_CONFIRMATION_EMAIL: Login failed.")
            sys.exit(1)

        print(rv, data)

        rv, data = mailbox.select('INBOX')
        if rv == 'OK':
            url = process_mailbox(mailbox)

            if url:
                print(f'{user_details} - confirmation url found: {url}')
                break
            else:
                print(f'{user_details} confirmation url not found yet, waiting a bit more')

            mailbox.close()
            mailbox.logout()
        else:
            print("ERROR: Unable to open mailbox ", rv)
            mailbox.logout()

    return url
