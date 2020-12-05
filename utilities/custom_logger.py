import logging
import os

path_to_logs = os.path.join('.', 'logs', 'AutoTest.log')


class LogGen:

    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=path_to_logs, format='%(asctime)s: %(levelname)s: %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
