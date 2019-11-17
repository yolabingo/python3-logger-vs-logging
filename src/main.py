#/usr/bin/env python3

import logging

logging.basicConfig(level=logging.DEBUG)

logging.info(' * main.py * ')

# this creates module-level loggers in client.py
from app.client import Client

logging.info(" * main.py: Client().greet() ")
Client().greet()

