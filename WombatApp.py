__version__ = 1.0

import pyrebase
import logging
import os
import datetime


class firebase(object):
    def __init__(self, username, password):
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
        self.user = username
        self.passwd = password

    def add_players(self):
        self.firedb.child('wombatapp').child('players').update({'current': False,
                                                                 'firstname': 'Tom',
                                                                 'surname': 'Lowe',
                                                                 'id': 2,
                                                                 'nickname': 'Fingers'})

    def user_info(self):
        try:
            logger.info(self.auth.get_account_info(self.user['idToken']))
        except Exception as err:
            logger.error(err)

    def login_user(self):
        try:
            self.user = self.auth.sign_in_with_email_and_password(self.user, self.passwd)
            logger.info("User successfully logged in %s", self.user['email'])
            self.user_info()
        except Exception as err:
            logger.error(err)

    def create_user(self):
        # Creating user
        logger.info("Creating new user")
        try:
            self.auth.create_user_with_email_and_password(self.user, self.passwd)
            logger.info("New user created %s", self.user)

        except Exception as err:
            logger.error("errrrrror: %s", err)


def main():
    # firebase("ash@hot.com", "123456").create_user()
    # firebase("ash@hot.com", "123456").login_user()
    firebase("ash@hot.com", "123456").add_players()

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
