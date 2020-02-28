import configparser
from pprint import pprint
import os

from helpers.logger import info, warn, error, debug

from objects import exceptions
from objects.dataType import Config

def createConfig():
    config_ = configparser.ConfigParser()
    config_['REDIS'] = {
        'host': 'localhost',
        'port': '6379',
        'user': 'redis',
        'password': ''
    }

    config_['DATABASE'] = {
        'host': 'localhost',
        'port': '3306',
        'user': 'root',
        'password': ''
    }

    config_['BANCHO'] = {
        'banchoAPIBaseURL': 'http://localhost:5001',
        'cheesegullAPI': 'http://storage.ripple.moe'
    }

    config_['DISCORD'] = {
        'secretKey': ''
    }

    with open('config.ini', 'w') as f:
        config_.write(f)

class configUtils:
    def __init__(self):
        self._config = configparser.ConfigParser()
        if os.path.isfile('config.ini'):
            self._config.read('config.ini')
            info('Found config file.')
            if not self.checkConfig():
                raise exceptions.BadConfigFile()
        else:
            warn('configHelper: Config file not found. Generating one with default settings ...')
            createConfig()
            info('configHelper: Please edit the config then open again')
            raise exceptions.BadConfigFile()

    def readConfig(self):
        res = Config()
        # Redis
        res.redis.host = self._config['REDIS']['host']
        res.redis.port = self._config['REDIS']['port']
        res.redis.username = self._config['REDIS']['user']
        res.redis.password = self._config['REDIS']['password']
        # Database
        res.mysql.host = self._config['DATABASE']['host']
        res.mysql.port = self._config['DATABASE']['port']
        res.mysql.username = self._config['DATABASE']['user']
        res.mysql.password = self._config['DATABASE']['password']
        # Pep.py API
        res.peppy.baseUrl = self._config['BANCHO']['banchoAPIBaseURL']
        res.peppy.cheesegullAPI = self._config['BANCHO']['cheesegullAPI']
        # Discord Secret
        res.discord.secretKey = self._config['DISCORD']['secretKey']

        info('configHelper: Reading config data: ')
        for section in self._config:
            for key in self._config[section]:
                print(section + ':' + key + ' = ' + self._config[section][key])

        return res

    def checkConfig(self):
        try:

            self._config.get('REDIS', 'host')
            self._config.get('REDIS', 'port')
            self._config.get('REDIS', 'user')

            self._config.get('DATABASE', 'host')
            self._config.get('DATABASE', 'port')
            self._config.get('DATABASE', 'user')
            self._config.get('DATABASE', 'password')

            self._config.get('BANCHO', 'banchoAPIBaseURL')
            
            self._config.get('DISCORD', 'secretKey')
            info('configHelper: Checking config. Looks fine I guess ?')
            return True
        except Exception as err:
            error('configHelper: Missing Args')
            return False





