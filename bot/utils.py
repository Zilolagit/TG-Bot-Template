from db.models import User


async def save_user(**kwargs):
    user = await User.get(kwargs.get('id'))
    if not user:
        await User.create(**kwargs)