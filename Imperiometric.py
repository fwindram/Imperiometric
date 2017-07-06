# Imperiometric.py
# Skeletorfw
# 06/07/17
#
# Python 3.4.1
#
# Bot to convert between metric & imperial units on demand.

import logging

import praw
from prawcore import exceptions

# Set up logging
# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create logfile handler
handler = logging.FileHandler('log/SSCHED.out')
handler.setLevel(logging.INFO)  # File logging level

# Create formatter and add to handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)

# CONFIG
reddit = praw.Reddit('bot1')

# Try to import banlist, but continue if not present.
try:
    from banlist import banlist
except ImportError:
    logger.debug('No banlist present.')

