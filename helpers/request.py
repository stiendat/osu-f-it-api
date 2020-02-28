from urllib.request import urlopen
from objects.dataType import User

def getUserData(userID = None, discordID = None):
    if (userID == None) and (discordID == None):
        pass
