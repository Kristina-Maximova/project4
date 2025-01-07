import os
import logging


path_to_logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "my_logs.log")
# print(path_to_logfile)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
                    filename=f"{path_to_logfile}",
                    filemode="w",
                    encoding="utf-8")

masks_logger = logging.getLogger()
utils_logger = logging.getLogger()