from aiogram import Bot, types
import config


class TelegramBot:
    def __init__(self):
        self.API_TOKEN = config.TOKEN
        self.channel_id = config.chanel_id
        self. bot = Bot(token=self.API_TOKEN, parse_mode=types.ParseMode.HTML)

    async def send_message(self, text: str):
        await self.bot.send_message(self.channel_id, text)
