from fastapi import FastAPI
from app.database.models import async_session
from app.database.models import User, Dict
from sqlalchemy import select



app = FastAPI()


async def get_user_dict(user_id: int):
    async with async_session() as session:
        query = select(Dict).where(Dict.user == user_id)
        result = await session.scalar(query)
        return result


@app.get('/users/{user_id}')
async def read_user_dict(user_id: int):
    db_data = await get_user_dict(user_id)
    return db_data
