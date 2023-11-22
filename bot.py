import asyncio
from aiogram import Bot,Dispatcher
from handlers import client, none_command, admin, teacher
from database import client_info,teacher_info
from create_bot import bot, dp 

async def main():
    print('Bot online....')
    client_info.sql_start()
    

    dp.include_router(client.router)
    dp.include_router(admin.router_admin)
    dp.include_router(teacher.router_teacher)
    await dp.start_polling(bot) 
    

    






if __name__=='__main__':
    asyncio.run(main())