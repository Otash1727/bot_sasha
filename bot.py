import asyncio
from aiogram import Bot,Dispatcher
from handlers import client
from database import client_info 


async def main():
    bot=Bot('5970463019:AAEZjWTh0TvAS3q2-N08zyG-2UMBxhpzzgk')
    dp=Dispatcher()
    print('Bot online....')
    client_info.sql_start()

    dp.include_router(client.router)


    await dp.start_polling(bot) 
    

    






if __name__=='__main__':
    asyncio.run(main())