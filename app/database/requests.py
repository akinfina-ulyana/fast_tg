from app.database.models import async_session
from app.database.models import User, Dict
from sqlalchemy import select


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def save_to_database(user_question, bot_answer, user):
    async with async_session() as session:
        translation = Dict(fraze=user_question, answer=bot_answer, user=user)
        session.add(translation)
        await session.commit()


async def get_user_dict(user_id: int):
    async with async_session() as session:
        query = select(Dict).where(Dict.user == user_id)
        result = await session.scalar(query)
        return result


"""
async def give_dict(user):
    async with async_session() as session:
        result = 
        await session.commit()
"""










