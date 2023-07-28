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
        self.headers = {'Authorization': f'Token {config.API_token}'}
        self.username = ''
        self.is_massage = False

    def check_new_messages(self):
        self.new_message = False
        self.is_massage = False
        response = requests.get(self.url)
        if response.status_code == 200:
            self.new_message = True
            data = json.loads(response.text)
            if data['message']['type'] == 'reply_user':
                self.dialog_id = data['message']['conversation']
                user_id = data['message']['from']
                user_url = f'https://api.carrotquest.io/users/{user_id}'
                user_json = json.loads(requests.get(user_url, headers=self.headers).text)
                self.username = user_json["data"]['props']['$name']
                try:
                    sup = data['message']['assignee']['id']
                    for name in config.sup_names:
                        if sup == name:
                            self.sup = config.sup_names.get(name)
                            self.is_massage = True
                except:
                    self.sup = None
                    self.is_massage = True

