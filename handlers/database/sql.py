import asyncio
import asyncpg
import logging

from data.config import PG_USER, PG_PASS, host


async def create_db():
    create_db_cmd = open("create_db.sql", "r").read()
    logging.info("Connecting to DB")
    con: asyncpg.Connection = await asyncpg.connect(
        user=PG_USER,
        password=PG_PASS,
        host=host
    )
    await con.execute(create_db_cmd)
    logging.info("Table has been created")
    await con.close()


async def create_pool():
    return await asyncpg.create_pool(
        user=PG_USER,
        password=PG_PASS,
        host=host
    )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
