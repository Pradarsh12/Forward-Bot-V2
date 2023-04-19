from dotenv import load_dotenv
from os import environ, path

load_dotenv()

if path.exists("bot_config.py"):
    from bot_config import Config
else:
    class Config(object):
        APP_ID = int(environ.get("23161785", None))
        API_HASH = environ.get("72e2c9ff7f587a134a46fe99708e3194", None)
        BOT_TOKEN = environ.get("6220875828:AAHwgQEBdnsqOopD9GhgvCW04P_C68I1OSc", None)
        BOT_WORKERS = int(environ.get("BOT_WORKERS", 40))
        SUDO_USERS = environ.get("6010304291", None)
        DB_URI = environ.get("mongodb+srv://projectnv:projectnv321@cluster0.wieiqcz.mongodb.net/?retryWrites=true&w=majority", None)
        SESSION_NAME = environ.get("SESSION_NAME", "test")
        MULTI_USER_MODE = environ.get('MULTI_USER_MODE', '').lower() in ['true', '1']
