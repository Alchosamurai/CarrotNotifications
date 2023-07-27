import asyncio
from aiogram import Bot, types
import config
import requests
import json

class CarrotBot:
    def __init__(self):
        self.api_token = config.API_token
        self.app_id = config.AppID
        self.url = f'https://realtime-services.carrotquest.io/longpoll/conversation_reply.{self.app_id}?auth_token={self.api_token}'
        self.chat_url = "https://carrotquest.io/panel/57562/conversations/"
        self.dialog_id = ''
        self.sup = ''
        self.new_message = False

    def check_new_messages(self):
        self.new_message = False
        response = requests.get(self.url)
        if response.status_code == 200:
            self.new_message = True
            data = json.loads(response.text)
            if data['message']['type'] == 'reply_user':
                self.dialog_id = data['message']['conversation']
                try:
                    sup = data['message']['assignee']['name']
                    for name in config.sup_names:
                        if sup == name:
                            self.sup = name
                except:
                    self.sup = None

