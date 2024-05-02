from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from fastapi import FastAPI
import sqlite3
"""
engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)
"""
app = FastAPI()

conn = sqlite3.connect('sqlite+aiosqlite:///db.sqlite3')

from fastapi import HTTPException

@app.get("/user/{user_id}")
async def read_item(user_id: int):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE id = ?', (item_id,))
    item = cursor.fetchone()
    cursor.close()
    if user_id is None:
        raise HTTPException(status_code=404, detail="U havent")
    return {"item": item}

conn.close()