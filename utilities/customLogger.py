import logging
import os

print("**********************************test_customLogger"+os.getcwd())

class LogGen:

    @staticmethod  # we can directly call w/o creating an object so we do not need self
    def loggen():
        logging.basicConfig(
            filename="\\automation.log",level=logging.INFO,
            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
