import configparser
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = 'bnn_config.ini'

def get_config(section):
    config = configparser.ConfigParser()
    config.read(f'{ROOT_DIR}/{CONFIG_FILE}')
    sender_email = config[section]['sender_email']
    recipient_email = config[section]['recipient_email']
    password = config[section]['password']

    return sender_email, recipient_email, password
