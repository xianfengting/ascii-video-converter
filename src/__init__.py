
import logging
import sys

formatter = logging.Formatter("[%(name)s][%(asctime)s][%(threadName)s][%(levelname)s]:%(message)s")
logger = logging.getLogger("monitor")
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)
logger.addHandler(sh)
