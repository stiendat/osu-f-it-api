import redis

with open('Danger.log', 'w+', encoding='UTF-8') as f:
    LOG_FILE = f

VERSION = '0.1 BETA'
LOG_LEVEL = 'debug'
REDIS = redis.Redis()
CONFIG = None