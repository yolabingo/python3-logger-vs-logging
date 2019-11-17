import logging

logging.info(' * app.client imported * ')

LOGGER = logging.getLogger(f"[{__name__}]")

LOGGER.info(' * app.client imported * ')


class Client:

    def greet(self):
        LOGGER = logging.getLogger('[Client.greet]')
        LOGGER.info(' * logger from Client.greet() * ')
        logging.info(' * logging from Client.greet() * ')

