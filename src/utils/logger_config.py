import os

def setup_logger(name):
    import logging

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(f"{log_dir}/pipeline.log")
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
