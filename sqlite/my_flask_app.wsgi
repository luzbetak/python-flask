#!/usr/local/bin/python3.8

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/store/www/sqlite/')
from my_flask_app import app as application
application.secret_key = 'anything you wish'

