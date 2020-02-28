from objects import glob

from helpers.logger import debug, info, warn, error, printWelcomeMessage
from helpers.configHelper import configUtils


printWelcomeMessage()                                                                               

####### LOAD CONFIG 
glob.CONFIG = configUtils().readConfig()

