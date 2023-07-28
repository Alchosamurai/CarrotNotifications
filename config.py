import os
from dotenv import load_dotenv

load_dotenv('keys.env')
TOKEN = str(os.getenv('tg_token'))
chanel_id = os.getenv('chat_id')

AppID = os.getenv('app_id')
API_token = os.getenv('app_token')

sup_names ={
    "119775": os.getenv('teg_N')
}

