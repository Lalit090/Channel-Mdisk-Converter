import os

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "27962408"))
API_HASH = os.environ.get("API_HASH", "31b63794f777a53d316196671310c947")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5908573063:AAEmgaAPTAQuxKpEP5JVO-X2B8tWxskz2o8")
DROPLINK_API = os.environ.get("DROPLINK_API")
MDISK_API = os.environ.get("MDISK_API", "qkCcEKPCRz6JR6TGTqD)
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split(",")) if os.environ.get("-1001883099272") else []
DATABASE_NAME = os.environ.get("DATABASE_NAME", "MdiskConvertorBotpro")
DATABASE_URL = os.environ.get("mongodb://Lalit905016:Lalit9050@ac-2jltdyh-shard-00-00.szfkpqd.mongodb.net:27017,ac-2jltdyh-shard-00-01.szfkpqd.mongodb.net:27017,ac-2jltdyh-shard-00-02.szfkpqd.mongodb.net:27017/?ssl=true&replicaSet=atlas-q6fdpn-shard-0&authSource=admin&retryWrites=true&w=majority ")
WEBSITE = os.environ.get('WEBSITE')

#  Optionnal variables
INCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("INCLUDE_DOMAIN").split(",")) if os.environ.get("INCLUDE_DOMAIN") else []
EXCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("EXCLUDE_DOMAIN").split(",")) if os.environ.get("EXCLUDE_DOMAIN") else []
CHANNELS = is_enabled((os.environ.get('CHANNELS', "True")), True)
CHANNEL_ID = list(int(i.strip()) for i in os.environ.get("CHANNEL_ID").split("-1001806065563")) if os.environ.get("CHANNEL_ID") else []
FORWARD_MESSAGE = is_enabled((os.environ.get('FORWARD_MESSAGE', "True")), True)
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://github.com/CyniteOfficial/Channel-Mdisk-Converter")
USERNAME = os.environ.get("USERNAME", "CyniteBackup")
HEADER_TEXT = os.environ.get("HEADER_TEXT", '')
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", '')
BANNER_IMAGE = os.environ.get("BANNER_IMAGE", '')
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = is_enabled((os.environ.get('LINK_BYPASS', "False")), False)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU = True if HEROKU_API_KEY and HEROKU_APP_NAME else False
