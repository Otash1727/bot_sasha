import asyncio
from create_bot import bot,dp,router


async def main():
    print('Bot online....')

from handlers import client
@dp.message(Command('start'))





if __name__=="__main__":
    asyncio.run(main());