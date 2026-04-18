import logging
import os

def setup_logging(log_file="test.log"):
    folder = "logs"
    os.makedirs(folder, exist_ok= True)
    file_path = f"{folder}/{log_file}"

    logger = logging.getLogger("automation_logger")
    logger.setLevel(logging.INFO)


    if  not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
        logger.handlers.clear()
        file_handler = logging.FileHandler(file_path, mode="a")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    print(f"Logging setup complete → {file_path}")
    logger.propagate = True
    return logger
