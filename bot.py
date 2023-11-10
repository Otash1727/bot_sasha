import asyncio
from aiogram import Bot,Dispatcher
from handlers import client, none_command
from database import client_info 


async def main():
    bot=Bot('6881326098:AAEbpDodIFDdQwUHn_rqUFfVvZNUMrXu2j0')
    dp=Dispatcher()
    print('Bot online....')
    client_info.sql_start()

    dp.include_router(client.router)
    #dp.include_router(none_command.router2)

    await dp.start_polling(bot) 
    

    






if __name__=='__main__':
    asyncio.run(main())