import logging

logging.info(' * app.client imported * ')
module_logger = logging.getLogger(f"[{__name__}]")
module_logger.info(' * app.client imported * ')

class Client:

    class_logger = logging.getLogger(f"[{__name__}.Client class]")
    class_logger.info(' * app.client.Client class defined * ')

    def __init__(self):
        self.logger = logging.getLogger(f"[{__name__}.Client instance]")
        self.logger.info(' * app.client.Client instance created * ')

    def greet(self):
        self.logger.info(' * from Client.greet() to instance logger* ')
        logging.info(' * from Client.greet() to root logger * ')

