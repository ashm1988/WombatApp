__version__ = 1.0

import pyrebase
import logging
import os
import datetime


class firebase(object):
    def __init__(self):
        config = {
            "apiKey": "AIzaSyBubZ6XTgOPmKPt8tbkdgtW_XGvgvwU6ho",
            "authDomain": "dynamowombatapp.firebaseapp.com",
            "databaseURL": "https://dynamowombatapp.firebaseio.com",
            "projectId": "dynamowombatapp",
            "storageBucket": "dynamowombatapp.appspot.com",
            "messagingSenderId": "294522566163",
            "appId": "1:294522566163:web:7b4f0ff6ae668121"
        }

        firebase = pyrebase.initialize_app(config)
        self.auth = firebase.auth()
        self.firedb = firebase.database()

    def create_user(self, username, password):
        # Creating user
        logger.info("Creating new user")
        try:
            self.auth.create_user_with_email_and_password(username, password)
            logger.info("New user created %s", username)
        except Exception as err:
            logger.error("errrrrror: %s", err)


def main():
    firebase().create_user("ash@hot.com", "123456")


if __name__ =='__main__':

    # set logging
    logfile_directory_name = 'LogFiles'
    logfile_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), logfile_directory_name)
    if not os.path.exists(logfile_directory):
        os.makedirs(logfile_directory)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    fh = logging.FileHandler(os.path.join(logfile_directory, '%s.log' % datetime.date.today().strftime("%Y%m%d")))
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    logger.addHandler(fh)
    main()
