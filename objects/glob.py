import redis

with open('Danger.log', 'w+', encoding='UTF-8') as f:
    LOG_FILE = f

LOG_LEVEL = 'debug'
REDIS = redis.Redis()