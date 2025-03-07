from bot.dispatchers import dp
from bot.handlers.foods import food_router
from bot.handlers.main import main_router
from bot.handlers.set_language import language_router

dp.include_routers(
    *[
        main_router,
        food_router,
        language_router
      ]
)