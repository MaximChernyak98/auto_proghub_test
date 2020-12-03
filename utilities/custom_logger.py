import logging


class LogGen:

    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=".\\logs\\AutoTest.log",
                            format='%(asctime)s: %(levelname)s: %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
