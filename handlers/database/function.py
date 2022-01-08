import asyncio

from asyncpg import Connection

from loader import db


class DBCommands:
    pool: Connection = db
    ADD_NEW_USER = 'INSERT INTO users()'
