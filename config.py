from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "6435225"))
    API_HASH = environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6774817827:AAEoLh3IktJ6gpDywo_0X80V6i45PWZJwZ0") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://heroku123456abc:wcadzyz8s6@cluster0.ngkzc2f.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", "1356815354").split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
