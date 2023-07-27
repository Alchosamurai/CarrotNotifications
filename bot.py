import asyncio
from aiogram import Bot, types
import config
import requests
import json

API_TOKEN = config.TOKEN
CHANNEL_ID = config.chanel_id # это должен быть int, например -1006666666666

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)


async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)


async def main():
    API_token = config.API_token
    app_id = config.AppID

    url = f'https://realtime-services.carrotquest.io/longpoll/conversation_reply.{app_id}?auth_token={API_token}'

    while True:
        operator = ''
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            if data['message']['type'] == 'reply_user':
                dialog = data['message']['conversation']

                try:
                    name = data['message']['assignee']['name']
                    if name == "Никита":
                        operator = '@Nrock24'
                    await send_message(CHANNEL_ID, f'{operator}, в кэрроте ответили\n https://carrotquest.io/panel/57562/conversations/{dialog}')
                except:
                    await send_message(CHANNEL_ID,
                                       f'В кэрроте новое сообщение\n https://carrotquest.io/panel/57562/conversations/{dialog}')

        print(response.text)



if __name__ == '__main__':
    asyncio.run(main())

