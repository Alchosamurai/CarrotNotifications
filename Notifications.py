import TeleBot
import CarrotBot
import asyncio

async def main():
    telegram = TeleBot.TelegramBot()
    carrot = CarrotBot.CarrotBot()

    while True:
        carrot.check_new_messages()
        if carrot.new_message and carrot.is_massage:
            if carrot.sup is None:
                message = f'В кэрроте новое сообщение от <b>{carrot.username}</b>\n {carrot.chat_url}{carrot.dialog_id}'
                await telegram.send_message(message)
            else:
                message = f'{carrot.sup}, в кэрроте ответ от <b>{carrot.username}</b>\n {carrot.chat_url}{carrot.dialog_id}'
                await telegram.send_message(message)



if __name__ == '__main__':
    asyncio.run(main())
