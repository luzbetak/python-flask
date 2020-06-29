#!/usr/bin/env python3.8

import logging
import sys
import site

site.addsitedir('/home/store/venv/lib/python3.8/site-packages')

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/store/www/plot')

from app import app as application
application.secret_key = 'anything you wish'

