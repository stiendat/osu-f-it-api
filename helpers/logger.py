import logging
from colorlog import ColoredFormatter
from objects.glob import LOG_LEVEL
# import helpers.extendLogger

# #########################
# # Logging
# logging.basicConfig(
#     format='[%(asctime)s] [%(levelname)s] [THREAD_ID %(thread)d] [PROCESS_ID %(process)d] :%(message)s',
#     level=logging.DEBUG
#     )
# #########################

logging.root.setLevel(logging.DEBUG)
formatter = ColoredFormatter('[%(asctime)s] [%(levelname)s] [THREAD_ID %(thread)d] [PROCESS_ID %(process)d] :%(message)s')
stream = logging.StreamHandler()
stream.setFormatter(formatter)
logger = logging.getLogger('basicLogger')
logger.addHandler(stream)
logger.setLevel(getLogLevel(LOG_LEVEL))

def getLogLevel(loglevel):
    if loglevel == 'warn':
        return logging.WARN
    elif loglevel == 'debug':
        return logging.DEBUG
    elif logging == 'error':
        return logging.ERROR
    else:
        return logging.INFO

def info(logData, danger = None):
    logging.info(str(logData))

def warn(logData, danger = None):
    logging.warning(str(logData))

def debug(logData, danger = None):
    logging.debug(str(logData))