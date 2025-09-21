import logging
import os

def get_logger():
  logger = logging.getLogger("QA-Logger")

  if not logger.handlers:  # supaya handler ga dobel
    logger.setLevel(logging.DEBUG)  # global level, biar DEBUG juga bisa masuk ke file

    formatter = logging.Formatter(
      "%(asctime)s - %(levelname)s - %(message)s"
    )

    # console handler (INFO ke atas)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    # pastikan folder logs ada
    os.makedirs("logs", exist_ok=True)

    # file handler (DEBUG ke atas)
    file_handler = logging.FileHandler("logs/test.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

  return logger
