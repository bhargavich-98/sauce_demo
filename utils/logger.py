import logging
import os

def get_logger(name=__name__, level=logging.INFO):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s | %(levelname)-7s | %(name)s | %(message)s')

    os.makedirs("reports", exist_ok=True)
    fh = logging.FileHandler("reports/test.log")
    fh.setFormatter(formatter)
    fh.setLevel(level)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(level)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
