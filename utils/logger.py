import logging
import os

def setup_logging(log_file):
    folder = "logs"
    os.makedirs(folder, exist_ok= True)
    file_path = f"{folder}/automation.log"

    root_logger = logging.getLogger()  #log_file
    root_logger.setLevel(logging.INFO)

    already_added = any(
        isinstance(h, logging.FileHandler)
        and 
        getattr(h, 'baseFilename', '') == os.path.abspath(file_path)
        for h in root_logger.handlers
    )

    if not already_added:
        file_handler = logging.FileHandler(file_path, mode="a")
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(name)-20s | %(filename)s:%(lineno)-8d | %(funcName)s() | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")

        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

  
    return logging.getLogger(log_file)
