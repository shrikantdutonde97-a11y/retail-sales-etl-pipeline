import logging
from pathlib import Path


def setup_logger():
    """
    Configure and return a logger.
    """

    # Project root
    project_root = Path(__file__).resolve().parent.parent

    # Logs folder
    logs_folder = project_root / "logs"

    # Log file
    log_file = logs_folder / "pipeline.log"

    # Create logger
    logger = logging.getLogger("etl_logger")

    # Set logging level
    logger.setLevel(logging.INFO)

    # Create file handler
    file_handler = logging.FileHandler(log_file)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    # Prevent duplicate handlers
    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger

