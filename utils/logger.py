import logging

def setup_logging(log_file):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger