import logging
import os

path_to_logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "my_logs.log")
# print(path_to_logfile)
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
#                     filename=f"{path_to_logfile}",
#                     filemode="w",
#                     encoding="utf-8")

masks_logger = logging.getLogger()
masks_handler = logging.FileHandler(f"{path_to_logfile}", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
masks_handler.setFormatter(file_formatter)
masks_logger.addHandler(masks_handler)
masks_logger.setLevel(logging.DEBUG)

utils_logger = logging.getLogger()
utils_handler = logging.FileHandler(f"{path_to_logfile}", mode="w", encoding="utf-8")
utils_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
utils_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_handler)
utils_logger.setLevel(logging.DEBUG)
